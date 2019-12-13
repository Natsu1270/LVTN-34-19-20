from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField
