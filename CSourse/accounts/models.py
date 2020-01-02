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
        return self.username

    @property
    def require_activation_by_admin(self):
        return self.require_activation == self.ACTIVATION_ADMIN

    @property
    def require_activation_by_user(self):
        return self.require_activation == self.ACTIVATION_USER

    def set_email(self, new_email):
        self.email = UserManager.normalize_email(new_email)
        self.email_hash = hash_email(new_email)













