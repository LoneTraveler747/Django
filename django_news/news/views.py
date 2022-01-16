from django.shortcuts import redirect, render

from .forms import CommentForm
from . models import *
from django.http import Http404
from django.shortcuts import render, get_object_or_404  , redirect

def index(reqest):
    posts = Post.objects.all()
    #select * from Post
    contex_obj = {'posts':posts}
    return render(reqest, 'news/index.html', 
                context = contex_obj)

def post_detail(request, id_post):
    try:
        post = Post.objects.get(id = id_post,)
    except Post.DoesNotExist:
        raise Http404('Статья не найдена')

    context = {'post': post, 'form':CommentForm}
    return render(request, 'news/post_detail.html', context = context)

def tags_list(requset):
    tags = Tag.objects.all()
    context_teg={'tags': tags}
    return render(requset, 'news/tags_list.html', context = context_teg)

def add_comment(request, id_post):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, id = id_post)
    if form.is_valid():
        comment = Comment()
        comment.text = form.cleaned_data['text']
        comment.author = request.user
        comment.fk_post = post
        comment.save()
    return redirect(post.get_absolute_url())
   