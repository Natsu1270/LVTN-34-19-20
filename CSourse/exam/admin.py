from django.contrib import admin
from .models import ExamAsset, Exam, AbilityExam


admin.site.register([Exam, ExamAsset, AbilityExam])
