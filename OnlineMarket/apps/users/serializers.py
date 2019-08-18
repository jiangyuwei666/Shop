from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     pass

    class Meta:
        model = User
        fields = ("id", "username", "name", "phone", "password")


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = "__all__"


##############################################
# class RegSerializers(serializers.ModelSerializer):
#     pwd2 = serializers.CharField(max_length=256, min_length=4, write_only=True)
#     tel = serializers.CharField(max_length=11, min_length=11)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'pwd2', 'tel')
#
#     def validate(self, attrs):
#         if attrs['pwd2'] != attrs['password']:
#             raise serializers.ValidationError('两次密码输入不一致')
#         del attrs['pwd2']
#         return attrs
#
#
# class LogSerializers(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=6)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#     def validate(self, attrs):
#         user_obj = User.objects.filter(username=attrs['username']).first()
#         if user_obj:
#             # check_password　可以将加密后的密码与输入的密码进行对比
#             if attrs['password'] == user_obj.password:
#                 return attrs
#         raise serializers.ValidationError('用户名或密码错误')
