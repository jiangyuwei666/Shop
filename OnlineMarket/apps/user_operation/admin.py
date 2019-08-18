from django.contrib import admin

from apps.user_operation import models
from apps.utils.BaseAdmin import BaseAdmin


class UserFavAdmin(BaseAdmin):
    list_display = ['id', 'user', 'goods', 'add_time']


class UserCommentAdmin(BaseAdmin):
    list_display = ['id', 'user', 'goods', 'msg_type', "message", 'file', 'add_time']


class UserAddressAdmin(BaseAdmin):
    list_display = ['id', 'address', 'signer_name', 'signer_phone', 'add_time']


admin.site.register(models.UserFav, UserFavAdmin)
admin.site.register(models.UserComment, UserCommentAdmin)
admin.site.register(models.UserAddress, UserAddressAdmin)
