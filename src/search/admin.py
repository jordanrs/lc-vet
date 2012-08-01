from django.contrib import admin
from search.models import *

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(SearchKeyword, SearchKeywordAdmin)
