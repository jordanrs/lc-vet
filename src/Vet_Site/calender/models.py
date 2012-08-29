from django.db import models

class Event (models.Model):
    title = models.CharField(max_length = 100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length = 25)
    
    def __unicode__(self):
        return self.title