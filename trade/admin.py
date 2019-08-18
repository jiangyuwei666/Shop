from django.contrib import admin

from apps.trade import models
from apps.utils.BaseAdmin import BaseAdmin


class ShoppingCartAdmin(BaseAdmin):
    list_display = ['id', 'user', 'goods', 'goods_nums']


class OrderInfoAdmin(BaseAdmin):
    list_display = ['id', 'user', 'order_sn', "trade_no", 'pay_status', 'order_mount', 'pay_time',
                    'address', 'signer_name', 'signer_phone']


class OderGoodsAdmin(BaseAdmin):
    list_display = ['id', 'order', 'goods', 'goods_nums', 'add_time']


admin.site.register(models.ShoppingCart, ShoppingCartAdmin)
admin.site.register(models.OrderInfo, OrderInfoAdmin)
admin.site.register(models.OrderGoods, OderGoodsAdmin)
