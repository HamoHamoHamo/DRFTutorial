# Generated by Django 3.1.5 on 2022-02-15 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(blank=True, max_length=16, null=True, verbose_name='시작시간')),
                ('finish_date', models.CharField(blank=True, max_length=16, null=True, verbose_name='종료시간')),
                ('ip', models.CharField(max_length=20, verbose_name='아이피')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
