from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details'),  # Add trailing slash
]
