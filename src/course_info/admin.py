from django.contrib import admin
from course_info.models import *

class PastPaperInline(admin.StackedInline):
    model = PastPaper

class CourseSectionInline(admin.StackedInline):
    model = CourseSection
    
class NotesInline(admin.StackedInline):
    model = Note

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
               CourseSectionInline,
               PastPaperInline,            
               NotesInline,
               ]
        
class LecturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)