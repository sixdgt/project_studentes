from django.urls import path
from . import  views

urlpatterns = [
    path('create/', views.student_create, name='student-create')
]