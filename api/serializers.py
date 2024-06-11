from rest_framework import serializers
from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields =  ['id', 'name', 'email', 'phone_number', 'address' , 'profile_picture']