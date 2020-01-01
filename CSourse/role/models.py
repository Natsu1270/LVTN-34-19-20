from django.db import models
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class Role(Group):
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=30, blank=True)

