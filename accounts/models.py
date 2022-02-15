from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError('must have user username')
        user = self.model(
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, username, password=None):
        user = self.create_user(
            password=password,
            username=username,
            name=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        unique=True, default='', max_length=100, null=False, blank=False)
    name = models.CharField(default='', max_length=100,
                            null=False, blank=False)
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    


    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field

    class Meta:
        db_table = 'auth_user'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


    def __str__(self):
        return self.username
