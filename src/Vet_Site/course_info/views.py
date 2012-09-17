from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, redirect
from vet_site.course_info.models import *
from vet_site.course_info.forms import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import datetime, random, sha
from django.core.mail import send_mail


# gonna have to use filter to produce a query set of results and get to get one single entry

def index(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render_to_response("courses.html", locals(), context_instance=RequestContext(request))

@login_required
def course_by_year(request, year):    
    courses = get_list_or_404(Course, study_year = year)
    return render_to_response("course_by_year.html", locals(), context_instance=RequestContext(request))

@login_required    
def course_detail(request, year, course_slug):
    course = get_object_or_404(Course, study_year = year, slug = course_slug)
    return render_to_response("course_detail.html", locals(), context_instance=RequestContext(request))

@login_required    
def course_section(request, year, course_slug, course_section):
    course = get_object_or_404(Course, study_year = year, slug = course_slug)
    course_section_slug = course_section
    course_section = get_object_or_404(CourseSection, slug = course_section)
    return render_to_response("course_section.html", locals(), context_instance=RequestContext(request))

@login_required    
def lecturers(request):
    return render_to_response("lecturers.html", {"lecturers" : Lecturer.objects.all(), "request" : request}, context_instance=RequestContext(request))

@login_required
def lecturer_detail(request, lecturer):
    lecturer_info = get_object_or_404(Lecturer, slug = lecturer)
    return render_to_response("lecturer_detail.html", locals(), context_instance=RequestContext(request))

@login_required
def contact(request):
    info_settings = InfoSetting.objects.all()
    vet_reps = ClassRep.objects.filter(school = VET_SCHOOL).order_by("year")
    medic_reps = ClassRep.objects.filter(school = MED_SCHOOL).order_by("year")
    college_contacts = CollegeContact.objects.all()
    return render_to_response("contact.html", locals(), context_instance=RequestContext(request))

@login_required
def events(request):
    return render_to_response("calender.html", locals(), context_instance=RequestContext(request))

@login_required
def dontpanic(request):
    sections = DontPanicSection.objects.all().order_by("position")
    return render_to_response("dontpanic.html", locals(), context_instance=RequestContext(request))

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid() :
            username = form.clean_username()
            password = form.clean_password2()
            
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+username).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            user = form.save()
            #  user.is_active = False
            user.save()
            profile = UserProfile(user=user,
                                      activation_key=activation_key,
                                      key_expires=key_expires)
            profile.save()
            
            user = authenticate(username=username, password=password)
            login(request, user)
            #do stuff
            return HttpResponseRedirect("/")
            
    else:
        form = UserCreateForm()
    return render_to_response("registration/register.html", {"form" : form }, context_instance=RequestContext(request))