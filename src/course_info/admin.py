from django.contrib import admin
from course_info.models import *

class CourseSectionInline(admin.StackedInline):
    model = CourseSection
    extra = 2    
    filter_horizontal = ['lecturers'] 
    prepopulated_fields = {"slug": ("topic",)}
    fieldsets = (
                 (None, {'fields': [],}),
                 ('Information', {'fields': ['topic', 'tips', 'description',  'lecturers', 'slug'], 'classes':['collapse']})
    )
    
class CourseFileInline(admin.StackedInline):
    model = CourseFile
    extra = 2
    radio_fields = {'type': admin.HORIZONTAL}
    fieldsets= (
                (None, {'fields': [],}),
                ('File Information', {'fields': ['name', 'year', 'created_by', 'course_section', 'type'], 'classes':['collapse'],})
    )
    
class CourseAdmin(admin.ModelAdmin):  
    
    model = Course
    radio_fields = {'study_year': admin.HORIZONTAL, 'term': admin.HORIZONTAL, 'difficulty':admin.HORIZONTAL }
    save_on_top = True         
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
               CourseSectionInline,           
               CourseFileInline,
               ]
        
    #List display data
    list_display = ('name', 'study_year', 'num_course_sections', 'num_course_files')
    
    def num_course_sections(self, obj):
        total = obj.coursesection_set.all()
        return total.__len__()
    num_course_sections.short_description = "No. Course Sections"
    
    def num_course_files(self, obj):
        total = obj.coursefile_set.all()
        return total.__len__()
    num_course_files.short_description = "No. Course Files"    
    
class LecturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)