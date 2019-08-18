from datetime import datetime

from django.db import models


class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = ((1, "一级类目"),
                     (2, "二级类目"),
                     (3, "三级类目"),)

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.CharField(max_length=50, choices=CATEGORY_TYPE, verbose_name="类别级别", help_text="类别级别")
    # 通过"self"字段实现无线分类（自己做自己的外键）
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父类目级别",
                                        on_delete=True, related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航栏", help_text="是否导航栏")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, on_delete=True, null=True, blank=True, verbose_name="商品类目")
    # 商品的编号
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品的唯一编号", unique=True)
    name = models.CharField(max_length=200, verbose_name="商品名称")
    # 点击数
    click_num = models.IntegerField(default=0, verbose_name="商品点击数")
    # 销量
    sold_num = models.IntegerField(default=0, verbose_name="商品销量")
    # 库存数量
    goods_num = models.IntegerField(default=0, verbose_name="商品库存数量")
    # 商品价格
    price = models.FloatField(default=0, verbose_name="商品价格")
    # 商品简介
    goods_intro = models.TextField(default="", verbose_name="商品简介")
    # 富文本编辑器
    # goods_desc = UEditorField()
    # 是否包邮
    ship_free = models.BooleanField(default=False, verbose_name="是否包邮")
    # 封面图片
    goods_front_img = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="展示图片")
    # 是否为热卖商品,可以用于首页显示
    is_hot = models.BooleanField(default=False, verbose_name="是否新品")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加事件")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品详情界面的商品展示图
    """
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="图片")
    add_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "商品详情图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name + ' 商品详情图'


class Banner(models.Model):
    """
    轮播商品（首页展示的图片）
    """
    goods = models.ForeignKey(Goods, on_delete=True, verbose_name="商品")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播索引")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name + ' 商品轮播图'
