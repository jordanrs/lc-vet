from django.db import models
from django.contrib.auth.models import User
import datetime
#from markdown import markdown

class Category(models.Model):
    title = models.CharField(max_length=255, help_text="Maximum 250 characters")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically created from title. Muat be unique")
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/categories/{0}/".format(self.slug,)
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
        
class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
              (LIVE_STATUS, 'Live'),
              (DRAFT_STATUS, 'Draft'),
              (HIDDEN_STATUS, 'Hidden'),
              )
    
    title = models.CharField(max_length = 255)
    excerpt = models.TextField(blank = True)
    body = models.TextField()
    excerpt_html = models.TextField(editable=False, blank = True)
    body_html = models.TextField(editable=False, blank = True)
    pub_date = models.DateTimeField(default = datetime.datetime.now)
    slug = models.SlugField(unique_for_date = 'pub_date')
    author = models.ForeignKey(User)
    comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default = 1)
    categories = models.ManyToManyField(Category)
 
    def save(self):
#        self.body_html = markdown(self.body)
#        if self.excerpt:
#            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()
    
    def __unicode__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return "/weblog/%s/%s" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']