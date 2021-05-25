from django.db import models
from accounts.models import Account

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    userName = models.CharField(max_length=50, blank=True)
    userSurname = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=250)
    demoUrl = models.URLField(blank=True, max_length=500)
    otherUrl = models.URLField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Id: " + str(self.id) + " " + ", user: " + self.user.name
