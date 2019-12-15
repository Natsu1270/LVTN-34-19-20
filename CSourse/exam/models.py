from django.db import models


class Exam(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    status = models.BooleanField(blank=True)
    max_score = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    answer = models.CharField(max_length=200)
    examAsset = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class QuestionChoice(models.Model):
    content = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class AbilityExam(models.Model):
    exam = models.OneToOneField(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.name



