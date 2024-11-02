from django.urls import path
from . import views


app_name = 'Blog'


urlpatterns = [
    path('', views.blog_list, name='blog_list')
]
