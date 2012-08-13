from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from vet_site.course_info.models import Course, Lecturer, CourseSection
from django.template import RequestContext

# gonna have to use filter to produce a query set of results and get to get one single entry

def index(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def course_list(request):
    courses = Course.objects.all()
    return render_to_response("courses.html", locals(), context_instance=RequestContext(request))

def course_by_year(request, year):    
    courses = get_list_or_404(Course, study_year = year)
    return render_to_response("course_by_year.html", locals(), context_instance=RequestContext(request))
    
def course_detail(request, year, course_slug):
    course = get_object_or_404(Course, study_year = year, slug = course_slug)
    return render_to_response("course_detail.html", locals(), context_instance=RequestContext(request))
    
def course_section(request, year, course_slug, course_section):
    course = get_object_or_404(Course, study_year = year, slug = course_slug)
    course_section_slug = course_section
    course_section = get_object_or_404(CourseSection, slug = course_section)
    return render_to_response("course_section.html", locals(), context_instance=RequestContext(request))
    
def lecturers(request):
    return render_to_response("lecturers.html", {"lecturers" : Lecturer.objects.all(), "request" : request}, context_instance=RequestContext(request))

def lecturer_detail(request, lecturer):
    lecturer_info = get_object_or_404(Lecturer, slug = lecturer)
    return render_to_response("lecturer_detail.html", locals(), context_instance=RequestContext(request))