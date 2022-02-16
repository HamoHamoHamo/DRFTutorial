from django.shortcuts import get_object_or_404
from .models import Attendance
from rest_framework import serializers
#from accounts.serializers import UserAttendanceSerializer
from accounts.serializers import UserNameSerializer
from accounts.models import User

class CheckUserAttendanceSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField()
    # user = UserNameSerializer()
    #user = serializers.ReadOnlyField(source="user.name")
    class Meta:
        model = Attendance
        fields = ('id', 'user','datetime', 'ip')
        #exclude = ['start_date', 'finish_date']

    
    # def create(self, validated_data):
        
    #     return Attendance.objects.create(**validated_data)

class AttendanceListSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField()
    # user = UserNameSerializer()
    user = serializers.ReadOnlyField(source="user.name")
    class Meta:
        model = Attendance
        fields = ('id', 'user','datetime', 'ip')
        #exclude = ['start_date', 'finish_date']

    
    # def create(self, validated_data):
        
    #     return Attendance.objects.create(**validated_data)