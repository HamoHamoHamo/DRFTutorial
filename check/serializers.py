from .models import Attendance
from rest_framework import serializers

class CheckAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        #exclude = ['start_date', 'finish_date']
    
    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)