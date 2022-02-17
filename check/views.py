from django.db.models import Q
from accounts.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from dj_rest_auth.registration.views import RegisterView
from .models import Attendance
from .serializers import CheckUserAttendanceSerializer, AttendanceListSerializer
from rest_framework import generics

from rest_framework import viewsets

from datetime import datetime

from check import serializers



@api_view(['POST'])
def check(request):
    
    # ip 확인
    print("REQUEST", "DATA", request.data['ip'])
    ip = request.data['ip']
    now = str(datetime.now())[:16]
    serializer = CheckUserAttendanceSerializer(data={'user': request.user.pk, 'ip': ip, 'datetime': now})
    print("serializer : ", serializer)
    print("serializer", serializer)
    if serializer.is_valid():
        serializer.save()
    else:
        
        print("ERROR", serializer.errors, serializer.error_messages)
    
    return Response(serializer.data)

class AttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceListSerializer
    

    def get_queryset(self):
        queryset = Attendance.objects.filter(datetime__contains=self.kwargs['month']).order_by("user", "datetime")
        return queryset

@api_view(['get'])
def profile(request):
    today = str(datetime.now())[:10]
    attendance = Attendance.objects.filter(Q(datetime__contains=today) & Q(user=request.user.pk))
    print("출석", attendance)
    serializer = AttendanceListSerializer(attendance, many=True)
    # print("serializer", serializer)
    
    return Response(serializer.data)

class AttendanceDestroyAPIView(generics.DestroyAPIView):
    serializers = CheckUserAttendanceSerializer
    queryset = Attendance.objects.all()
