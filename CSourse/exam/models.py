from django.db import models


class Exam(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    status = models.BooleanField(blank=True)
    max_score = models.IntegerField()


class ExamAsset(models.Model):
    code = models.CharField(max_length=200)


class Question(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    answer = models.CharField(max_length=200)
    examAsset = models.ForeignKey(ExamAsset, on_delete=models.CASCADE)


class AbilityExam(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)


