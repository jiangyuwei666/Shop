from django.contrib import admin

# Register your models here.
from apps.users import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', "name", "phone", 'email', 'gender', 'birthday', 'head_img')


admin.site.register(models.UserProfile, UserAdmin)
