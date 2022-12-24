from django.shortcuts import render,get_object_or_404
from .models import *
import datetime
import markdown2

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
    date_now  = datetime.datetime.now()

    context={
        'blog':blogs,
        'D_N':date_now

    }
    return render(request,'main/blog.html',context)

def convert(f):

        html= markdown2.markdown(f)
        return html
def page(request,pk):
    blogs = get_object_or_404(blog,id=pk)
    des = blogs.long_decsription
    des2 = convert(des)
    date_now  = datetime.datetime.now()


    context = {
        'blogs':blogs,
        'des':des2,
        'D_N':date_now

    }
    return render(request,'main/page.html',context)