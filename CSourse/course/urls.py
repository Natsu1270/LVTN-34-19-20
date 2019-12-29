from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<str:course_code>', views.course_detail, name='course_detail'),
    path('learn/<str:course_code>', views.course_learn, name='course_learn')
]
