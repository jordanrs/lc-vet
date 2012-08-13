from django.contrib import admin
from vet_site.course_info.models import *

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
                ('File Information', {'fields': ['name', 'year', 'created_by', 'course_section', 'file', 'type'], 'classes':['collapse'],})
    )
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

    #    field = super(CourseFileInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'course_section':
            test = request.path.split("/")[-2]
            if test == "add":
                kwargs["queryset"]= CourseSection.objects.none()
                return db_field.formfield(**kwargs)
            kwargs["queryset"]= CourseSection.objects.filter(course=test)
            return db_field.formfield(**kwargs)
        return super(CourseFileInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CourseAdmin(admin.ModelAdmin):  
    
    model = Course
    radio_fields = {'study_year': admin.HORIZONTAL, 'term': admin.HORIZONTAL, 'difficulty':admin.HORIZONTAL, 'school': admin.HORIZONTAL }
    save_on_top = True         
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
               CourseSectionInline,           
               CourseFileInline,
               ]
        
    #List display data
    list_display = ('name', 'study_year', 'school', 'num_course_sections', 'num_course_files')
    
    def num_course_sections(self, obj):
        total = obj.coursesection_set.all()
        return total.__len__()
    num_course_sections.short_description = "No. Course Sections"
    
    def num_course_files(self, obj):
        total = obj.coursefile_set.all()
        return total.__len__()
    num_course_files.short_description = "No. Course Files"    
 
#    def get_form(self, request, obj=None, **kwargs):
#        # just save obj reference for future processing in Inline
#        request._obj_ = obj
#        return super(CourseAdmin, self).get_form(request, obj, **kwargs)    
       
class LecturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)