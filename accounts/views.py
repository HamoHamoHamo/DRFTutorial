from .serializers import UserProfileSerializer
from .models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from accounts import serializers
from rest_framework.permissions import AllowAny

from dj_rest_auth.registration.views import RegisterView

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.middleware.csrf import get_token


# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class EnsureCsrf(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         # print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
#         print(get_token(request))
#         print("TOKKK", request.META['CSRF_COOKIE'])
#         return Response(request.META['CSRF_COOKIE'])

# @api_view(('get',))
# @ensure_csrf_cookie
# def ensure_csrf(request):
#     if request.method == "get":
#         users = User.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
#         return Response(serializer.data)
#     return

# 회원가입
# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserList(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
#         return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny],)
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
        return Response(serializer.data)

@api_view(['GET'])
def user_detail(request):
    print(request.user)
    user = request.user
    print(user.id,type(user))
    serilalizer = UserProfileSerializer(user)
    return Response(serilalizer.data)

# class RegisterView(RegisterView):
#     serializer_class = 