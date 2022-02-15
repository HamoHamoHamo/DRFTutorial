from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from accounts import serializers
from rest_framework.permissions import AllowAny
from dj_rest_auth.registration.views import RegisterView
from .models import Attendance
from .serializers import CheckAttendanceSerializer

from datetime import datetime



@api_view(['POST'])
def check(request):
    
    # ip 확인
    print("REQUEST", "DATA", request.data['ip'])
    ip = request.data['ip']
    now = str(datetime.now())[:16]
    serializer = CheckAttendanceSerializer(data={'user': request.user.pk, 'ip': ip, 'datetime': now})
    print("serializer", serializer)
    if serializer.is_valid():
        serializer.save()
    else:
        
        print("ERROR", serializer.errors, serializer.error_messages)
    
    return Response(serializer.data)
