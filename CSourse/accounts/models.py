from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager

from datetime import date
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import HStoreField

from role.models import Role
from .utils import hash_email


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def get_by_username(self, username):
        return self.get(username=username)

    def get_by_email(self, email):
        return self.get(email_hash=hash_email(email))

    def get_by_username_or_email(self, login):
        if "@" in login:
            return self.get(email_hash=hash_email(login))
        return self.get(username=login)


class User(AbstractUser):

    ACTIVATION_NONE = 0
    ACTIVATION_USER = 1
    ACTIVATION_TEACHER = 2
    ACTIVATION_TA = 3
    ACTIVATION_ADMIN = 4

    SUBSCRIPTION_NONE = 0
    SUBSCRIPTION_NOTIFY = 1
    SUBSCRIPTION_ALL = 2

    SUBSCRIPTION_CHOICES = [
        (SUBSCRIPTION_NONE, _("No")),
        (SUBSCRIPTION_NOTIFY, _("Notify")),
        (SUBSCRIPTION_ALL, _("Notify with e-mail")),
    ]

    email = models.EmailField(max_length=200, blank=True, db_index=True)
    email_hash = models.CharField(max_length=32, unique=True)
    require_activation = models.PositiveIntegerField(default=ACTIVATION_NONE)
    roles = models.ManyToManyField(Role, related_name="user_role")
    is_deleting_account = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    @property
    def require_activation_by_admin(self):
        return self.require_activation == self.ACTIVATION_ADMIN

    @property
    def require_activation_by_user(self):
        return self.require_activation == self.ACTIVATION_USER

    def set_email(self, new_email):
        self.email = UserManager.normalize_email(new_email)
        self.email_hash = hash_email(new_email)


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

    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='account/profile/avatar')
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    social = HStoreField(default=dict)

    university = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=20, blank=True)

    allow_viewing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()

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










