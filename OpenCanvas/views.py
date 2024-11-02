from django.http import HttpResponse 
from django.shortcuts import render,redirect


def Index(request):
    return redirect('Blog:blog_list')