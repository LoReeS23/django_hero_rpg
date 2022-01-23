from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from user.forms import SEX_CHOICE


class MyUser(AbstractBaseUser):
    nickname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)
    sex = models.CharField(max_length=20, choices=SEX_CHOICE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

