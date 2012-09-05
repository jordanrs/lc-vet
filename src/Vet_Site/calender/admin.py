from django.contrib import admin
from django.conf import settings
from vet_site.calender.models import *

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)