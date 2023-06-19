from rest_framework import serializers
from app_students.models import StudentModel
from app_courses.models import CourseModel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["course_name", "course_code"]
        model = CourseModel
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["first_name", "middle_name", "last_name", "email", "contact", "address", "course", "current_degree",]
        model = StudentModel