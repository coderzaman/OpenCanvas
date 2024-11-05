from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details'),  # Add trailing slash
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('un_liked/<pk>/', views.un_liked, name='un_liked_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='update_blog'), 
    path('profile/<pk>/', views.public_profile, name='profile'), 
]
