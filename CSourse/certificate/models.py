from django.db import models


class CertificateType(models.Model):
    name = models.CharField(max_length=200)
    expired_time = models.Field
    created_date = models.DateField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    granted_date = models.DateField()
    created_date = models.DateField()
    modified_date = models.DateField()
    certificate_type = models.ManyToManyField(CertificateType)

    def __str__(self):
        return self.name



