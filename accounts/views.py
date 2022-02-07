from .serializers import UserSerializer, UserListSerializer
from .models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from accounts import serializers
from rest_framework.permissions import AllowAny

from dj_rest_auth.registration.views import RegisterView

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny],)
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
        return Response(serializer.data)

# class RegisterView(RegisterView):
#     serializer_class = 