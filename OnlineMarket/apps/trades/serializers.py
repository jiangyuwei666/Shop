from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth import get_user_model
from apps.trades.models import ShoppingCart, OrderGoods, OrderInfo
from apps.goods.serializers import GoodsSerializer

User = get_user_model()


class ShoppingCartSerializer(serializers.ModelSerializer):

    img = serializers.ImageField(source="goods.goods_front_img")
    price = serializers.FloatField(source="goods.price")
    name = serializers.CharField(source="goods.name")

    class Meta:
        model = ShoppingCart
        fields = ("id", "img", "price", "name", "goods_nums", "user", "goods")


class ShoppingCartDetailSerializer(serializers.ModelSerializer):

    img = serializers.ImageField(source="goods.goods_front_img")
    price = serializers.FloatField(source="goods.price")
    name = serializers.CharField(source="goods.name")
    class Meta:
        model = ShoppingCart
        fields = ("id", "img", "price", "name", "goods_nums", "user", "goods")


class OrderGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGoods
        fields = ("user", "goods", "goods_nums")


class OrderGoodsDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderInfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.name")
    class Meta:
        model = OrderInfo
        fields = ("user", "order_sn", "order_mount", "name", "address", "signer_name", "signer_phone")


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"
