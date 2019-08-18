from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True,
                            verbose_name="昵称")  # 通过手机注册，所以可以为空，不然无法存表(可以在注册时候设置相应的表单)
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    phone = models.CharField(max_length=11, default="", verbose_name="手机号")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别")
    # email = models.CharField(max_length=50, verbose_name="邮箱")
    head_img = models.ImageField(default="", upload_to="", verbose_name="用户头像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    通过邮箱验证登陆
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.CharField(max_length=50, verbose_name="邮箱")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
