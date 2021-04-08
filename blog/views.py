from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

def all_blogs(request):
    #blogs = Blog.objects.all()
    recent_blog_count = 4
    blogs = Blog.objects.order_by('-date')[:recent_blog_count]
    blog_count = Blog.objects.count
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'blog_count':blog_count, 'recent_blog_count':recent_blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
