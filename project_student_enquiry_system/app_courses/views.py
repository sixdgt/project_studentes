from django.shortcuts import render, redirect
from app_courses.forms import CourseCreateForm
from app_courses.models import CourseModel

# Create your views here.
def course_index(request):
    courses = CourseModel.objects.all()

    context = {
        "title": "SES | Courses", 
        "body_title": "Here are the courses details",
        "courses": courses
    }
    return render(request, 'courses/index.html', context)

def course_create(request):
    form = CourseCreateForm()
    context = {"form": form}

    if request.method == "POST":
        name = request.POST.get("course_name")
        code = request.POST.get("course_code")
        cm = CourseModel(course_name=name, course_code=code)
        cm.save()

        # cm = CourseModel()
        # cm.course_name = request.POST.get("course_name")
        # cm.course_code = request.POST.get("course_code")
        # cm.save()
        return redirect("course-index")

    return render(request, 'courses/create.html', context)

def course_edit(request):
    return render(request, 'courses/edit.html')

def course_show(request):
    return render(request, 'courses/show.html')