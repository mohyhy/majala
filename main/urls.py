from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.blog, name='blog'),
    path('page/<int:id>', views.page, name='page'),


]

