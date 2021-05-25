from django.db import models
from accounts.models import Account

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    userName = models.CharField(max_length=50)
    userSurname = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    isPublic = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
