from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, View, TemplateView
from BlogApp.models import Blog, Comment, Likes 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
import uuid
from BlogApp.forms import CommentForm
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
        blog_obj.slug = slugify(title) + "-" + str(uuid.uuid4())[:8]  # Shorten the UUID for a cleaner slug
        blog_obj.save()
        return redirect('index')
       

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog 
    template_name = 'BlogApp/blog_list.html'    
    # queryset = Blog.objects.order_by('-publish_date')

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('Blog:blog_details', slug)
        
    return render(request, 'BlogApp/blog_details.html', context={'blog':blog, 'comment_form':comment_form}) 
    