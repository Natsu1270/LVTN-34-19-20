from django.contrib import admin
from .models import Exam, AbilityExam, Question, QuestionChoice


admin.site.register([Exam, AbilityExam, Question, QuestionChoice])
