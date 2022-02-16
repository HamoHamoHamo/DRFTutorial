from django.db import models

from accounts.models import User

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance", null=True)
    datetime = models.CharField(verbose_name="체크시간", max_length=16, null=True, blank=True)
    ip = models.CharField(verbose_name="아이피", max_length=20,  null=False)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')