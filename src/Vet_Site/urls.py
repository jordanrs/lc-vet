from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

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
     
     #other
     (r'^contact/$', 'contact'),
     url(r'^events/$', 'events', name = "events"),
     (r'^register/$', 'register'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {"next_page" :"/"}) ,              
    )

urlpatterns += patterns('',
                     
                       (r'^password_change/$', 
                        'django.contrib.auth.views.password_change', 
                        {'template_name': 'accounts/password_change_form.html'}),

                       (r'^password_change/done/$', 
                        'django.contrib.auth.views.password_change_done', 
                        {'template_name': 'accounts/password_change_done.html'}),

                       (r'^password_reset/$', 
                        'django.contrib.auth.views.password_reset', 
                        {'template_name': 'accounts/password_reset_form.html',}),

                       (r'^password_reset/done/$', 
                        'django.contrib.auth.views.password_reset_done', 
                        {'template_name': 'accounts/password_reset_done.html'}),

                       (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                        'django.contrib.auth.views.password_reset_confirm', 
                        {'template_name': 'accounts/password_reset_confirm.html'}),

                       (r'^reset/done/$', 
                        'django.contrib.auth.views.password_reset_complete', 
                        {'template_name': 'accounts/password_reset_complete.html'}),

)

#EVERYTHIN MUST BE ABOVE THIS
urlpatterns += patterns('', 
      #catch all for flat pages
     (r'', include('django.contrib.flatpages.urls')),
)



