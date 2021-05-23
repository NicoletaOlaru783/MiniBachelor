from projects.models import Project
from questions.models import Question
from django.db import models

# Create your models here.


class Comment(models.Model):
    userName = models.CharField(max_length=50)
    userSurname = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    questionId = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.comment
