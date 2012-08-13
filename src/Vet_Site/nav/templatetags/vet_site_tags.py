from django import template
from vet_site.course_info.models import Course, CourseSection

register = template.Library()

@register.inclusion_tag('nav.html')
def nav_list(value):
    
    courses = Course.objects.order_by("study_year").all() 
    year1 = courses.filter(study_year = 1).order_by('school')
    year2 = courses.filter(study_year = 2).order_by('school')
    year3 = courses.filter(study_year = 3).order_by('school')
    year4 = courses.filter(study_year = 4).order_by('school')
    year5 = courses.filter(study_year = 5).order_by('school')
    year6 = courses.filter(study_year = 6).order_by('school')
    years = [ year1, year2, year3, year4, year5, year6]
    return locals()



