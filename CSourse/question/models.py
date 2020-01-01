from django.db import models
from exam.models import Exam


class Question(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    answer = models.CharField(max_length=200)
    examAsset = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.content + "-" + self.title


class QuestionChoice(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
