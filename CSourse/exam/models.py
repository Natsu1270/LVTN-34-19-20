from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=200)


class AbilityExam(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)


