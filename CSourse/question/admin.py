from django.contrib import admin
from .models import Question, QuestionChoice

admin.site.register([Question, QuestionChoice])
