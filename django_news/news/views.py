from django.shortcuts import render
from . models import *

def index(reqest):
    posts = Post.objects.all()
    #select * from Post
    contex_obj = {'posts':posts}
    return render(reqest, 'news/index.html', 
                context = contex_obj)

def post_detail(request, id_post):
    post = Post.objects.get(id = id_post)
    context = {'post': post}
    return render(request, 'news/post_detail.html', context = context)