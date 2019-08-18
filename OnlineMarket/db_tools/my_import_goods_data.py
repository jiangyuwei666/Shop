# -*- coding: utf-8 -*-

import sys
import os
import time
import hashlib

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OnlineMarket.settings")

import django

django.setup()

from apps.goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.my_product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.price = float(int(goods_detail["price"].replace("￥", "").replace("元", "")))
    goods.goods_intro = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_front_img = goods_detail["images"][0] if goods_detail["images"] else ""
    goods.goods_sn = hashlib.md5((str(int(time.time()))+goods.name).encode('utf-8')).hexdigest()

    category_name = goods_detail["categorys"][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detail["images"]:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()
