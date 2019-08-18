from django.contrib import admin

from apps.goods import models
from apps.utils.BaseAdmin import BaseAdmin


# Register your models here.


class GoodsAdmin(BaseAdmin):
    list_display = ("id", "name", "category", "goods_sn", "sold_num", "is_hot")
    list_editable = ["name", "sold_num", "is_hot", "category"]


class CategoryAdmin(BaseAdmin):
    list_display = ("id", "name", "code", "category_type", "parent_category")


class BannerAdmin(BaseAdmin):
    list_display = ("id", "goods", "index", "image")


admin.site.register(models.Goods, GoodsAdmin)
admin.site.register(models.GoodsCategory, CategoryAdmin)
admin.site.register(models.Banner, BannerAdmin)