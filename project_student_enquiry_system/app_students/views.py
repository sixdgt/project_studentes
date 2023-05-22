from django.shortcuts import render, redirect
from app_students.models import StudentModel
from app_students.forms import StudentCreateForm

# Create your views here.
def student_create(request):
    form = StudentCreateForm()
    context = {"form": form}

    if request.method == "POST":
        std = StudentCreateForm(request.POST)
        if std.is_valid():
            std.save()
            return redirect("student-index")
        return redirect("student-create")
    return render(request, 'students/create.html', context)

def student_index(request):
    students = StudentModel.objects.all()
    context = {
        "students" : students, 
        "title": "SES | Student List", 
        "body_title": "Here are the students list"
        }
    return render(request, "students/index.html", context)