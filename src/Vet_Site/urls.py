from django.conf.urls import patterns, include, url
import vet_site.course_info

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vet_Site.views.home', name='home'),
    # url(r'^vet_Site/', include('Vet_Site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^$', 'vet_site.course_info.views.index'),
     (r'^search/$', 'search.views.search'),
     
     # webblog stuff
     (r'^weblog/$', 'coltrane.views.entries_index'),
     (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\w{2})/(?P<slug>[-\w]+)/$','coltrane.views.entry_detail'),
          
     
)

urlpatterns += patterns('vet_site.course_info.views', 
      # courses
     (r'^courses/$', 'course_list'),
     (r'^courses/year-(?P<year>\d)/$', 'course_by_year'),
     (r'^courses/year-(?P<year>\d)/(?P<course_slug>[-\w]+)/$', 'course_detail'),
     (r'^courses/year-(?P<year>\d)/(?P<course_slug>[-\w]+)/(?P<course_section>[-\w]+)/$', 'course_section'),
     
     #lecturer
     (r'^lecturers/$', 'lecturers'),
     (r'^lecturers/(?P<lecturer>[-\w]+)/$', 'lecturer_detail'),
)

urlpatterns += patterns('', 
      #catch all for flat pages
     (r'', include('django.contrib.flatpages.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

