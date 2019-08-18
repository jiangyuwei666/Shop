from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth import get_user_model
from apps.trade.models import ShoppingCart, OrderGoods, OrderInfo
from apps.goods.serializers import GoodsSerializer

User = get_user_model()


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ("user", "goods", "goods_nums")


class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = ShoppingCart
        fields = "__all__"


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
    class Meta:
        model = OrderInfo
        fields = ("user", "order_sn", "order_mount", "is_pay")


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"
