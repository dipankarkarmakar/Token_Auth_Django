# # from rest_framework import serializers
# # from .models import File
# #
# # class FileSerializer(serializers.ModelSerializer):
# #     class Meta():
# #         model = File
# #         fields = ('file', 'remark', 'timestamp')
#
#
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
# from .models import Profile
#
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     username = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(min_length=8)
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#                                         validated_data['password'])
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#
from rest_framework import serializers
from .models import File
class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')