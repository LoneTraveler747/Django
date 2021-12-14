from django.contrib import admin
from django.db import models
from django.db.models.base import Model

# Register your models here.

from .models import Post, Comment, Tag

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0
#admin.site.register(Post)
#admin.site.register(Comment)
class TaginLine(admin.TabularInline):
    Model = Tag
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','text','author','pub_date')
    inlines = [CommentInLine]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','author','pub_date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    