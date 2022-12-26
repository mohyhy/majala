from django.shortcuts import render,get_object_or_404
from .models import *
import datetime
import markdown2

# Create your views here.
most = New.objects.filter(most_popular =True).order_by('-date_post')
trend = New.objects.filter(trending =True).order_by('-date_post')
print(trend[0])


def index(request):
    news = New.objects.filter(type='News').order_by('-date_post')
    date_now  = datetime.datetime.now()
    print(news)

    context={
        'news':news,
        'most':most,
        'trend':trend,
        'D_N':date_now.date(),
        'mostrend':trend[0]
    }
    return render(request,'main/index.html',context)


def blogs(request):
    blogs = New.objects.filter(type='Blogs').order_by('-date_post')
    
    date_now  = datetime.datetime.now()

    context={
        'blog':blogs,
        'most':most,
        'trend':trend,
        'D_N':date_now.date(),
        'mostrend':trend[0]


    }
    return render(request,'main/blog.html',context)

def convert(f):

        html= markdown2.markdown(f)
        return html
def page(request,pk):
    blogs = get_object_or_404(New,id=pk)
    des = blogs.long_decsription
    des2 = convert(des)
    date_now  = datetime.datetime.now()


    context = {
        'blogs':blogs,
        'des':des2,
        'D_N':date_now,
        'mostrend':trend[0]


    }
    return render(request,'main/page.html',context)

def section(request,cate):
    news = New.objects.filter(cate=cate).order_by('-date_post')

    return render(request,'main/section.html',{
        'f':cate,
        'blog':news,
        'most':most,
        'mostrend':trend[0]


    })

