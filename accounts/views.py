from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from check.models import Attendance
from datetime import datetime

from dj_rest_auth.registration.views import RegisterView

# @api_view(['GET'])
# @permission_classes([AllowAny],)
# def user_list(request):
#     if request.method == "GET":
#         users = User.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         print(serializer.data, "aSEEEEEEEEEEEEEEEEEEEEEE")
#         return Response(serializer.data)

# @api_view(['GET'])
# def user_detail(request):
#     print(request.user)
#     user = request.user
#     today = str(datetime.now())[:10]
#     attendance = Attendance.objects.filter(Q(datetime__contains=today) & Q(user=request.user.pk))
#     print("출석", attendance)
#     attendance_serializer = CheckUserAttendanceSerializer(attendance)
    
#     serializer = UserAttendanceSerializer(user, data={attendance:attendance})
#     print("SERIALIZER", serializer)
#     return Response(serializer.data)

# class RegisterView(RegisterView):
#     serializer_class = 