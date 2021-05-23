from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


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
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.name + " " + self.surname
