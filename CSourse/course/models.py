from django.db import models
from accounts.models import Teacher
from exam.models import AbilityExam


class Course(models.Model):
    STATIC_COURSE = 'sc'
    LIVE_COURSE = 'lc'
    MIXED_COURSE = 'mc'
    COURSE_TYPE_CHOICES = [
        (STATIC_COURSE, 'Static course'),
        (LIVE_COURSE, 'Live course'),
        (MIXED_COURSE, 'Mixed course'),
    ]

    BEGINNER = 'bg'
    INTERMEDIATE = 'im'
    ADVANCED = 'ad'
    MIXED = 'mx'

    COURSE_LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (MIXED, 'Mixed'),
    ]

    code = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='course/avatar', default=None)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=COURSE_TYPE_CHOICES)
    level = models.CharField(max_length=2, choices=COURSE_LEVEL_CHOICES, default=None)
    trainer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_date = models.DateField()
    open_date = models.DateTimeField()
    rate_score = models.FloatField(default=0)
    rate_num = models.IntegerField(default=0)
    ability_exam = models.ManyToManyField(AbilityExam, blank=True)

    def __str__(self):
        return self.name

