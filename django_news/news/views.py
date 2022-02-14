from django.shortcuts import redirect, render

from .forms import CommentForm, PostCreateForm, TagCreateForm, TagForm, UserUpdateForm
from . models import *
from django.http import Http404
from django.shortcuts import render, get_object_or_404  , redirect
from django.views.generic import View, ListView
from  . import forms

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

    context = {'post': post, 'form':CommentForm, 'tagform': TagForm}
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

class TagCreate(View):
    def get(self, request, *args, **kwargs):
        form = TagCreateForm()
        return render(request, 'news/tag_create_form.html', {'form':form})
    
    def post(self,request, *args, **kwargs):
        filled_form = TagCreateForm(request.POST)

        if filled_form.is_valid():
            filled_form.save()
            return redirect('tags_list_url')

        return render(request, 'news/tag_create_form.html', {'form':filled_form})

def add_tag(request, id_post):
    form = TagForm(request.POST)
    post = get_object_or_404(Post, id = id_post)
    if form.is_valid():
        post.tags.add(Tag.objects.get(pk = form.cleaned_data['tags']))
    return redirect(post.get_absolute_url())

class TagUpdate(View):
        def get(self, request, id_tag):
            tag = Tag.objects.get(pk=id_tag)
            form = TagCreateForm(instance=tag)
            return render(request, 'news/tag_update_form.html', context={'form': form, 'obj':tag})

        def post(self, request, id_tag):
            tag = Tag.objects.get(pk=id_tag)
            form = TagCreateForm(request.POST, instance=tag)
            
            if form.is_valid():
                form.save()
                tags = Tag.objects.all()
                context_teg={'tags': tags}
                return render(request, 'news/tags_list.html', context = context_teg)
            return render(request, 'news/tag_update_form.html', context={'form':form, 'obj': tag})

class TagDelete(View):
        def get(self, request, id_tag):
            tag = Tag.objects.get(pk=id_tag)
            return render(request, 'news/tag_delete_form.html', context={'obj': tag})

        def post(self, request, id_tag):
            tag = Tag.objects.get(pk=id_tag)
            tag.delete()
            tags = Tag.objects.all()
            context_teg={'tags': tags}
            return render(request, 'news/tags_list.html', context = context_teg)

class PostCreate(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        return render(request, 'news/post_create_form.html', {'form':form})
    
    def post(self,request, *args, **kwargs):
        filled_form = PostCreateForm(request.POST)

        if filled_form.is_valid():
            # post = Post()
            # post.title = filled_form.cleaned_data['title']
            # post.text = filled_form.cleaned_data['text']
            # post.author = request.user
            # post.save()
            new_post=filled_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect(new_post    )
            #return redirect(post.get_absolute_url())
        return render(request, 'news/post_create_form.html', {'form':filled_form})
    
class PostUpdate(View):
    def get(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        form = PostCreateForm(instance=post)
        return render(request, 'news/post_update_form.html', context={'form': form, 'obj':post})

    def post(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, 'news/post_update_form.html', context={'form':form, 'obj': post})


class PostDelete(View):
        def get(self, request, id_post):
            post = Post.objects.get(pk=id_post)
            return render(request, 'news/post_delete_form.html', context={'obj': post})

        def post(self, request, id_post):
            post = Post.objects.get(pk=id_post)
            post.delete()
            posts = Post.objects.all()
            contex_obj = {'posts':posts}
            return render(request, 'news/index.html', context = contex_obj)


class UserUpdateView(View):

    def get(self, request):
        data_obj = User.objects.get(username=request.user.username)
        bound_form = UserUpdateForm(instance=data_obj)
        return render(request, 'news/user_account.html', context={'form': bound_form, 'obj': data_obj})
    
    def post(self, request):
        data_obj = User.objects.get(username=request.user.username)
        bound_form = UserUpdateForm(request.POST, instance=data_obj)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('profile_detail_url')
        return render(request, 'news/user_account.html', context={'form': bound_form, 'obj':data_obj})

class UserPostsListView(ListView):
        model = Post
        template_name = 'news/posts_lists.html'

        def get_queryset(self):
            return Post.objects.filter(author = self.request.user).order_by('pub_date')