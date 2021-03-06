# Generated by Django 2.2.2 on 2019-07-01 11:48

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0006_auto_20190701_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_nums', models.IntegerField(default=1, verbose_name='购物车数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 7, 1, 19, 48, 31, 559361), verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=True, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(max_length=50, verbose_name='订单编号')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='支付编号')),
                ('is_pay', models.BooleanField(default=False, verbose_name='是否支付')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单总金额')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='支付时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 7, 1, 19, 48, 31, 560360), verbose_name='添加时间')),
                ('address', models.CharField(default='', max_length=100, verbose_name='收件地址')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='收件人姓名')),
                ('signer_phone', models.CharField(default='', max_length=11, verbose_name='收件人电话')),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_nums', models.IntegerField(default=0, verbose_name='商品数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 7, 1, 19, 48, 31, 561359), verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=True, to='goods.Goods', verbose_name='商品')),
                ('order', models.ForeignKey(on_delete=True, to='trades.OrderInfo', verbose_name='订单信息')),
            ],
            options={
                'verbose_name': '订单内的物品',
                'verbose_name_plural': '订单内的物品',
            },
        ),
    ]
