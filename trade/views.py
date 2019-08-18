import time
import hashlib

from rest_framework import viewsets, mixins, filters, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from apps.user_operation.models import UserAddress
from apps.trade.models import ShoppingCart, OrderGoods, OrderInfo
from apps.trade.serializers import ShoppingCartSerializer, ShoppingCartDetailSerializer, OrderGoodsSerializer, \
    OrderGoodsDetailSerializer, OrderInfoSerializer, OrderInfoDetailSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    """
    购物车
    """
    authentication_classes = []
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    @action(detail=False, methods=['get'])
    def get_shopping_cart(self, request):
        user = request.GET.get("user", "0")
        shopping_cart = ShoppingCart.objects.filter(user_id=user)
        res = ShoppingCartDetailSerializer(shopping_cart, many=True)
        return response.Response(res.data)

    @action(detail=False, methods=['post'])
    def add_shopping_cart(self, request):
        user = request.POST.get("user", "0")
        good = request.POST.get("good", "0")
        shopping_already = ShoppingCart.objects.filter(user_id=user, goods_id=good).first()
        if shopping_already:
            shopping_already.goods_nums += 1
            shopping_already.save()
        else:
            ShoppingCart.objects.create(user_id=user, goods_id=good)
        shopping = ShoppingCart.objects.filter(user_id=user)
        res = ShoppingCartDetailSerializer(shopping, many=True)
        return response.Response(res.data)

    @action(detail=False, methods=['get'])
    def delete_shopping_cart(self, request):
        user = request.GET.get("user", "0")
        shopping_id = request.GET.get("shopping", "0")
        shopping_already = ShoppingCart.objects.filter(id=shopping_id).first()
        if shopping_already:
            if shopping_already.goods_nums > 1:
                shopping_already.goods_nums -= 1
                shopping_already.save()
            else:
                ShoppingCart.objects.filter(id=shopping_id)[0].delete()
        shopping = ShoppingCart.objects.filter(user_id=user)
        res = ShoppingCartDetailSerializer(shopping, many=True)
        return response.Response(res.data)


class OrderInfoViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = OrderInfoSerializer

    @action(detail=False, methods=['get'])
    def get_orders(self, request):
        """
        返回所有订单
        """
        user = request.GET.get("user", "0")
        orders = OrderInfo.objects.filter(user_id=user)
        res = OrderInfoSerializer(orders, many=True)
        return response.Response(res.data)

    @action(detail=False, methods=['get'])
    def get_order(self, request):
        """
        返回一个订单
        """
        order = request.GET.get("order", "0")
        order_obj = OrderInfo.objects.filter(id=order)
        res = OrderInfoDetailSerializer(order_obj, many=True)
        return response.Response(res.data)

    @action(detail=False, methods=['post'])
    def add_order(self, request):
        user_id = request.POST.get("user", "0")
        addr_id = request.POST.get("addr", "0")
        hl = hashlib.md5()
        sn = str(int(time.time())) + user_id
        hl.update(sn.encode(encoding='utf-8'))
        order_sn = hl.hexdigest()
        # 收件人信息
        addr = UserAddress.objects.filter(id=addr_id).first()
        # 购物车里的东西
        shopping_goods = ShoppingCart.objects.filter(user_id=user_id)
        money = 0.0
        count = 0
        # 计算购物车里的金额
        for good in shopping_goods:
            count += 1
            money += good.goods.price * good.goods_nums
        print(type(money), money)
        print(type(order_sn), order_sn)
        print(type(addr.address), addr.address)
        print(type(addr.signer_phone), addr.signer_phone)
        print(type(addr.signer_name), addr.signer_name)
        order_obj = OrderInfo()
        print(1)
        order_obj.user_id = user_id
        print(2)
        order_obj.order_sn = order_obj.trade_no = order_obj
        print(3)
        order_obj.signer_name = addr.signer_name
        print(4)
        order_obj.signer_phone = addr.signer_phone
        print(5)
        order_obj.address = addr.address
        print(6)
        order_obj.order_mount = money
        print(7)
        order_obj.save()
        # order_obj = OrderInfo.objects.create(user_id=user_id, order_sn=order_sn, trade_no=order_sn, pay_status="cancel",
        #                                      address=addr.address, signer_phone=addr.signer_phone,
        #                                      signer_name=addr.signer_name, order_mount=money)
        # 创建订单内的商品
        for good in shopping_goods:
            order_good = OrderGoods()
            order_good.order_id = order_obj.id
            order_good.goods_id = good.goods.id
            order_good.goods_nums = good.goods_nums
        # 清空购物车
        print("***************************")
        ShoppingCart.objects.filter(user_id=user_id).delete()
        print("***************************")
        res = OrderInfoDetailSerializer(order_obj, many=True)
        print("***************************")
        return response.Response(res.data)

    @action(detail=False, methods=['get'])
    def delete_order(self, request):
        order = request.GET.get("order", "0")
        order_obj = OrderInfo.objects.filter(id=order).delete()
        res = OrderInfoDetailSerializer(order_obj, many=True)
        return response.Response(res.data)


class OrderGoodsViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    """
    订单和商品
    """
    authentication_classes = []
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializer

    @action(detail=False, methods=['get'])
    def get_order_goods(self, request):
        order = request.GET.get("order", "0")
        order_goods = OrderGoods.objects.filter(order=order)
        res = OrderGoodsDetailSerializer(order_goods, many=True)
        return response.Response(res.data)

    # @action(detail=False, methods=['get'])
    # def add_order_goods(self, request):
    #     order = request.GET.get("order", "0")
    #     good = request.GET.get("good", "0")
    #     goods_nums = request.GET.get("goods_nums", "0")
    #     OrderGoods.objects.create(order=order, goods_id=good, goods_nums=goods_nums)
    #     order_goods = OrderGoods.objects.filter(order=order)
    #     res = OrderGoodsDetailSerializer(order_goods, many=True)
    #     return response.Response(res.data)

    # @action(detail=False, methods=['get'])
    # def delete_order_goods(self, request):
    #     order = request.GET.get("order", "0")
    #     shopping_id = request.GET.get("shopping", "0")
    #     shopping_already = OrderGoods.objects.filter(id=shopping_id).first()
    #     if shopping_already:
    #         if shopping_already.goods_nums > 1:
    #             shopping_already.goods_nums -= 1
    #             shopping_already.save()
    #         else:
    #             OrderGoods.objects.filter(id=shopping_id).delete()
    #     shopping = OrderGoods.objects.filter(user_id=user)
    #     res = OrderGoodsDetailSerializer(shopping, many=True)
    #     return response.Response(res.data)
