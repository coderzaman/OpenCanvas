from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, View, TemplateView
from BlogApp.models import Blog, Comment, Likes 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.
def blog_list(request):
    return render(request, 'BlogApp/blog_list.html')


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'BlogApp/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')
    
    def form_valid(self, form):
       blog_obj = form.save(commit=False)
       blog_obj.author = self.request.user 
       title = blog_obj.blog_title
       blog_obj.slug = title.replace("","-") + "-" + str(uuid.uuid4())
       blog_obj.save()
       return redirect('index')
       
    