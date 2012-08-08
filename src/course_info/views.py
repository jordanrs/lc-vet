from django.shortcuts import render_to_response
from course_info.models import Course, Lecturer

def index(request):
    return render_to_response("index.html", {"request": request})

def course_list(request):
    return render_to_response("courses.html", {"courses" : Course.objects.all(), "request" : request})

def course_by_year(request, year):    
    return render_to_response("course_by_year.html", {"year" : year, "request" : request,})
    
def course_detail(request, year, course):
    return render_to_response("course_detail.html", {"year" : year, "request" : request, "course" : course})
    
def course_section(request, year, course, course_section):
    return render_to_response("course_section.html", {"year" : year, "request" : request, "course" : course, "course_section": course_section})
    
def lecturers(request):
    return render_to_response("lecturers.html", {"lecturers" : Lecturer.objects.all(), "request" : request})

def lecturer_detail(request, lecturer):
    return render_to_response("lecturer_detail.html", {"lecturer" : lecturer, "request" : request})