from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    NOT_SAY = 'N'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NOT_SAY, 'Rather not say')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, unique=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    fullname = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='/account/profile/avatar')
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.fullname or str(self.user)


class Trainee(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    about = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    major_field = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)





