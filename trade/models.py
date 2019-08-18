from datetime import datetime

from django.db import models

# 获取用户User模型的两种方法，推荐使用第一种
from django.contrib.auth import get_user_model
# from users.models import UserProfile

from apps.goods.models import Goods

# 获取User model
User = get_user_model()


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=True, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品")
    goods_nums = models.IntegerField(default=1, verbose_name="购物车数量")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return " "
        # return "{0}  {1}".format(self.goods.name, self.goods_nums)


class OrderInfo(models.Model):
    """
    订单
    """

    ORDER_STATUS = (
        ("success", "支付成功"),
        ("cancel", "待支付"),
    )

    user = models.ForeignKey(User, on_delete=True, verbose_name="用户")
    order_sn = models.CharField(max_length=50, verbose_name="订单编号")
    trade_no = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name="支付编号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="cancel", max_length=10, verbose_name="支付状态")
    is_pay = models.BooleanField(default=False, verbose_name="是否支付")
    order_mount = models.FloatField(default=0.0, verbose_name="订单总金额")
    pay_time = models.IntegerField(null=True, blank=True, verbose_name="支付时间")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="添加时间")

    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收件地址")
    signer_name = models.CharField(max_length=20, verbose_name="收件人姓名")
    signer_phone = models.CharField(max_length=11, verbose_name="收件人电话")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单内的商品
    """
    order = models.ForeignKey(OrderInfo, on_delete=True, verbose_name="订单信息")
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品")
    goods_nums = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(null=True, blank=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单内的物品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order)
