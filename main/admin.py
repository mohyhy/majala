from django.contrib import admin
from .models import *
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id','title','date_post', 'most_popular', 'trending' ,'type' )

admin.site.register(New,NewAdmin)
