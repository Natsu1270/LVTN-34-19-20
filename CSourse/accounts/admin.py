from django.contrib import admin
from .models import Profile, Trainee, Teacher
# Register your models here.

admin.site.register([Profile, Trainee, Teacher])
