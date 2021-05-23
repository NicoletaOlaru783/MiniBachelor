from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


from django.contrib.auth.hashers import make_password


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password, alias=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,)
        user.set_password(make_password(password))
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    username = None

    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.name + " " + self.surname
