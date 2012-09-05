from tastypie.resources import ModelResource
#from tastypie.authentication import SessionAuthentication
from tastypie.authentication import Authentication
from tastypie.authorization import DjangoAuthorization
from vet_site.calender.models import Event

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'events'
        # authentication = SessionAuthentication()
        authentication = Authentication()
        authorization = DjangoAuthorization()