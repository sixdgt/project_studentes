from django.urls import path
from . import  views

urlpatterns = [
    path('list/', views.student_index, name='student-index'),
    path('create/', views.student_create, name='student-create')
]