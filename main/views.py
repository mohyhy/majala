from django.shortcuts import render,get_object_or_404
from .models import *
import datetime
# Create your views here.

def index(request):
    news = New.objects.all()
    date_now  = datetime.datetime.now()
    context={
        'news':news,
        'D_N':date_now
    }
    return render(request,'main/index.html',context)


def blogs(request):
    blogs = blog.objects.all()
    context={
        'blog':blogs,
    }
    return render(request,'main/blog.html',context)


def page(request,pk):
    blogs = get_object_or_404(blog,id=pk)
    context = {
        'blogs':blogs
    }
    return render(request,'main/page.html',context)