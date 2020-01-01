from django.db import models


class Exam(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    status = models.BooleanField(blank=True)
    max_score = models.IntegerField()

    def __str__(self):
        return self.name


class AbilityExam(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.name



