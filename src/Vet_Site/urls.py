from django.conf.urls import patterns, include, url
import course_info

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vet_Site.views.home', name='home'),
    # url(r'^Vet_Site/', include('Vet_Site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^$', 'course_info.views.index'),
     (r'^search/$', 'search.views.search'),
     (r'^weblog/$', 'coltrane.views.entries_index'),
     
     (r'^courses/$', 'course_info.views.course_list'),
     (r'^courses/year-(?P<year>\d)/$', 'course_info.views.course_by_year'),
     (r'^courses/year-(?P<year>\d)/(?P<course>[-\w]+)/$', 'course_info.views.course_detail'),
     (r'^courses/year-(?P<year>\d)/(?P<course>[-\w]+)/(?P<course_section>[-\w]+)/$', 'course_info.views.course_section'),
     
     (r'^lecturers/$', 'course_info.views.lecturers'),
     (r'^lecturers/(?P<lecturer>[-\w]+)/$', 'course_info.views.lecturer_detail'),
     
     #catch all for flat pages
     (r'', include('django.contrib.flatpages.urls')),
     
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

