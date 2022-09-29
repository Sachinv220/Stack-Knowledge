from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.user} asks {self.question}"

class Answers(models.Model):
    post = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.posted_by} answers {self.post.question} by saying {self.answer}"