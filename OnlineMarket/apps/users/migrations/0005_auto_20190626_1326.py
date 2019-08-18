# Generated by Django 2.2.2 on 2019-06-26 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190626_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(default='', upload_to='', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 13, 26, 10, 215044), verbose_name='添加时间'),
        ),
    ]
