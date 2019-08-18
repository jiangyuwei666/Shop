from rest_framework import viewsets, mixins, filters, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from apps.user_operation.models import UserFav, UserAddress, UserComment
from apps.user_operation.serializers import UserFavSerializer, UserFavDetailSerializer, UserCommentSerializer, \
    UserCommentDetailSerializer, UserAddressSerializer, UserAddressDetailSerializer


class UserFavViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    authentication_classes = []
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer

    @action(detail=False, methods=['get'])
    def get_favs(self, request):
        user = request.GET.get("user", "0")
        favs = UserFav.objects.filter(user_id=user)
        res = UserFavDetailSerializer(favs, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['post'])
    def add_fav(self, request):
        user = request.POST.get("user", "0")
        good = request.POST.get("good", "0")
        fav_already = UserFav.objects.filter(user_id=user, goods_id=good)
        if fav_already:
            return response.Response("已经收藏了")
        UserFav.objects.create(user_id=user, goods_id=good)
        favs = UserFav.objects.filter(user_id=user)
        res = UserFavDetailSerializer(favs, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['get'])
    def delete_fav(self, request):
        user = request.GET.get("user", "0")
        good = request.POST.get("good", "0")
        fav_id = request.GET.get("fav", "0")
        UserFav.objects.filter(id=fav_id).delete()
        favs = UserFav.objects.filter(user_id=user)
        res = UserFavDetailSerializer(favs, many=True)
        return response.Response({"code": 1, "values": res.data})


class UserCommentViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    authentication_classes = []
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer

    @action(detail=False, methods=['get'])
    def get_comments(self, request):
        user = request.GET.get("user", "0")
        comments = UserComment.objects.filter(user_id=user)
        res = UserCommentDetailSerializer(comments, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['get'])
    def get_comment(self, request):
        comment_id = request.GET.get("comment", "0")
        comments = UserComment.objects.filter(id=comment_id)
        res = UserCommentDetailSerializer(comments, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['post'])
    def add_comment(self, request):
        user = request.POST.get("user", "0")
        good = request.POST.get("good", "0")
        msg_type = request.POST.get("type", "0")
        comment = request.POST.get("comment", "0")
        comment_already = UserComment.objects.filter(user_id=user, goods_id=good)
        if comment_already:
            return response.Response("已经评论了了")
        UserComment.objects.create(user_id=user, goods_id=good, message=comment, msg_type=msg_type)
        comments = UserComment.objects.filter(user_id=user)
        res = UserCommentDetailSerializer(comments, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['get'])
    def delete_comment(self, request):
        user = request.GET.get("user", "0")
        good = request.GET.get("good", "0")
        comment_id = request.GET.get("comment", "0")
        UserComment.objects.filter(id=comment_id).delete()
        comments = UserComment.objects.filter(user_id=user)
        res = UserCommentDetailSerializer(comments, many=True)
        return response.Response({"code": 1, "values": res.data})


class UserAddressViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    authentication_classes = []
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer

    @action(detail=False, methods=['get'])
    def get_addrs(self, request):
        user = request.GET.get("user", "0")
        addr = UserAddress.objects.filter(user_id=user)
        res = UserAddressDetailSerializer(addr, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['get'])
    def get_addr(self, request):
        addr_id = request.GET.get("addr", "0")
        addr = UserAddress.objects.filter(id=addr_id)
        res = UserAddressDetailSerializer(addr, many=True)
        return response.Response({"code": 1, "values": res.data})

    @action(detail=False, methods=['post'])
    def add_addr(self, request):
        user = request.POST.get("user", "0")
        addr = request.POST.get("addr", "0")
        sign_name = request.POST.get("sign_name", "0")
        sign_phone = request.POST.get("sign_phone", "0")
        UserAddress.objects.create(user_id=user, address=addr, signer_name=sign_name, signer_phone=sign_phone)
        addr = UserAddress.objects.filter(user_id=user)
        res = UserAddressDetailSerializer(addr, many=True)
        return response.Response({"code": 1, "values": res.data})

    # @action(detail=False, methods=['post'])
    # def update_addr(self, request):
    #     addr_id = request.POST.get("addr_id", "0")
    #     addr = request.POST.get("addr", "0")
    #     sign_name = request.POST.get("sign_name", "0")
    #     sign_phone = request.POST.get("sign_phone", "0")
    #     UserAddress.objects.filter(id=addr_id).update()
    #     addr = UserAddress.objects.filter(user_id=user)
    #     res = UserAddressSerializer(addr, many=True)
    #     return response.Response(res.data)

    @action(detail=False, methods=['get'])
    def delete_addr(self, request):
        user = request.GET.get("user", "0")
        addr_id = request.GET.get("addr", "0")
        UserAddress.objects.filter(id=addr_id).delete()
        addr = UserAddress.objects.filter(user_id=user)
        res = UserAddressDetailSerializer(addr, many=True)
        return response.Response({"code": 1, "values": res.data})
