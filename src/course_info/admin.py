from django.contrib import admin
from course_info.models import *

class CourseSectionInline(admin.StackedInline):
    model = CourseSection
    extra = 1
    
class CourseFileInline(admin.StackedInline):
    model = CourseFile
    extra = 1

class CourseAdmin(admin.ModelAdmin):  
    
    model = Course
              
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
               CourseSectionInline,           
               CourseFileInline,
               ]
        
class LecturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)