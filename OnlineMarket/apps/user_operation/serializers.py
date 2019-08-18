from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth import get_user_model
from apps.user_operation.models import UserFav, UserAddress, UserComment
from apps.goods.serializers import GoodsSerializer
from rest_framework.decorators import action

User = get_user_model()


class UserFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ("user", "goods", "id")


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = "__all__"


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ("user", "goods", "id")


class UserCommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserComment
        fields = "__all__"

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ("user", "id")


class UserAddressDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = "__all__"
