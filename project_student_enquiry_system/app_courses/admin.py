from django.contrib import admin
from app_courses.models import CourseModel

# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    # list_filter = ("course_name", "course_code")
    # search_fields = ("course_name", "course_code")
    # list_display = ("course_name", "course_code")
    list_display = list_filter = search_fields = ("course_name", "course_code")

admin.site.register(CourseModel, CourseModelAdmin)

# customizing admin panel title and name
admin.site.site_header = "Student Enquiry System"
admin.site.site_title = "SES"
admin.site.index_title = "Admin Panel"