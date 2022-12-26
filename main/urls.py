from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blogs, name='blog'),
    path('<int:pk>/', views.page, name='page'),
    path('section/<str:cate>/',views.section,name='section')


]

