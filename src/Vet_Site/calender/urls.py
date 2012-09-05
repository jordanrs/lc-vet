from django.conf.urls.defaults import *
from tastypie.api import Api
from vet_site.calender.api import EventResource

v1_api = Api(api_name = 'v1')
v1_api.register(EventResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)