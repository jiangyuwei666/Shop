from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from apps.goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, on_delete=True, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}收藏的{goods}".format(user=self.user.name, goods=self.goods.name)


class UserComment(models.Model):
    """
    用户留言（评论）
    """

    M = (
        (1, "好评"),
        (2, "中评"),
        (3, "差评"),
    )

    user = models.ForeignKey(User, on_delete=True, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品")
    msg_type = models.CharField(max_length=50, default=1, choices=M, verbose_name="啥评")
    message = models.TextField(default="系统默认好评", verbose_name="评论内容", help_text="评论内容")
    file = models.FileField(default="", upload_to="", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "用户品论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}对{good}的评论".format(user=self.user.name, good=self.goods.name)


class UserAddress(models.Model):
    """
    用户添加收件地址
    """
    user = models.ForeignKey(User, on_delete=True, verbose_name="用户")
    address = models.CharField(max_length=100, default="", verbose_name="收件地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="收件人姓名")
    signer_phone = models.CharField(max_length=11, default="", verbose_name="收件人电话")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "收件地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}收件地址{}".format(self.user.name, self.address)
