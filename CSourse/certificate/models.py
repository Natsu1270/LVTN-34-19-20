from django.db import models
from accounts.models import Profile


class CertificateType(models.Model):
    name = models.CharField(max_length=200)
    expired_time = models.Field
    created_date = models.DateField()


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    granted_date = models.DateField()
    created_date = models.DateField()
    modified_date = models.DateField()
    certificate_type = models.ManyToManyField(CertificateType)



