from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.course_index, name='course-index')
]