from django.contrib import admin
from .models import *
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id','title','cate','date_post', 'most_popular', 'trending','main','main2','type' )

admin.site.register(New,NewAdmin)
