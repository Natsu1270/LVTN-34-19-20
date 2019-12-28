from django.urls import path
from . import views


app_name = 'exam'
urlpatterns = [
    path('ability_exam/<str:course_code>', views.ability_exam, name='ability_exam'),
    path('take/<int:exam_id>', views.take_exam, name='take_exam')
]

