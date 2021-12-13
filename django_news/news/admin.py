from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Post, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0
#admin.site.register(Post)
#admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','text','author','pub_date')
    inlines = [CommentInLine]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','author','pub_date')