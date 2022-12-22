from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main/index.html')


def blog(request):
    return render(request,'main/blog.html')


def page(request,id):
    return render(request,'main/page.html')