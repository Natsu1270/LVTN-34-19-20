from django.contrib import admin
from .models import Certificate, CertificateType

admin.site.register([Certificate, CertificateType])
