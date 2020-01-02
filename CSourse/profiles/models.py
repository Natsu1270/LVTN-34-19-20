from django.db import models
from accounts.models import User
from django.conf import settings

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='account/profile/avatar')
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    university = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=20, blank=True)

    allow_viewing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar
        else:
            return settings.DEFAULT_AVATAR_URL

    @property
    def get_age(self):
        delta_day = date.today() - self.birth_date
        return delta_day.days // 365
