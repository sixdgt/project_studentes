from django.shortcuts import render
from app_students.models import StudentModel
from app_students.forms import StudentCreateForm

# Create your views here.
def student_create(request):
    form = StudentCreateForm()
    context = {"form": form}
    return render(request, 'students/create.html', context)