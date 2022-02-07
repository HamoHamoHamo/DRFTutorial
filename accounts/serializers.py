from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, max_length=100)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data() # username, password, email이 디폴트
        data_dict['name'] = self.validated_data.get('name', '')
        print("NNNNNNNNAAAAAAAMMMMMMEEEE", data_dict['name'])
        return data_dict

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['username', 'password', 'name']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']