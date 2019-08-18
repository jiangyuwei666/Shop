import time
import hashlib

from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from apps.users.serializers import UserSerializer, UserDetailSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


    @action(detail=False, methods=['post'])
    def login(self, request):
        user = request.POST["username"]

        password = request.POST["password"]
        print(user, password)
        # try:
        u = User.objects.get(username=user)
        if u.password == password:
            detail = UserDetailSerializer(u)
            hl = hashlib.md5()
            sn = str(int(time.time())) + str(u.id)
            hl.update(sn.encode(encoding='utf-8'))
            token = hl.hexdigest()
            if Token.objects.filter(user_id=u.id):
                Token.objects.filter(user_id=u.id).update(key=token)
            else:
                Token.objects.create(user_id=3, key=token)
            return Response({"code": 1, "values": detail.data})
        else:
            return Response("密码错误")
        # except:
        #     return Response("未注册")

    @action(detail=False, methods=['post'])
    def change_info(self, request):
        user_id = request.POST["user"]
        name = request.POST["name"]
        # birthday = request.POST["birthday"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        password = request.POST["password"]
        # head_img =
        User.objects.filter(id=user_id).update(name=name, password=password, phone=phone,
                                               gender=gender)
        user_obj = User.objects.filter(id=user_id)
        detail = UserDetailSerializer(user_obj, many=True)
        return Response({"code": 1, "values": detail.data})

    @action(detail=False, methods=['post'])
    def register(self, request):
        username = request.POST["phone"]
        phone = request.POST["phone"]
        name = request.POST["name"]
        password = request.POST["password"]
        gender = request.POST["gender"]
        if User.objects.filter(phone=phone):
            return Response("用户存在")
        # print(user, password)
        user_obj = User()
        user_obj.username = username
        user_obj.phone = phone
        user_obj.name = name
        user_obj.password = password
        user_obj.gender = gender
        user_obj.save()
        detail = UserDetailSerializer(user_obj)
        return Response({"code": 1, "values": detail.data})
