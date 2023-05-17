from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_courses"