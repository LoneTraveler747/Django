from django import db
import django
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import Case
from django.shortcuts import render
from django.shortcuts import reverse
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовк статьи')
    text = models.TextField(max_length=500,verbose_name='Текст')
    author = models.ForeignKey(auth_models.User, on_delete=CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',auto_now=True)

    class Meta:
        verbose_name= 'Статья'
        verbose_name_plural='Статьи'

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"id_post": self.pk})

    def __str__(self):
         return self.title

    def get_update_url(self):
        return reverse("post_update_url", kwargs={"id_post": self.pk})

    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"id_post": self.pk})

class Comment(models.Model):
    text = models.TextField(max_length=500,verbose_name='Текст')
    author = models.ForeignKey(auth_models.User, on_delete=CASCADE, verbose_name='Автор')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',auto_now=True)

    fk_post = models.ForeignKey(to=Post,on_delete=CASCADE, verbose_name='Статья'
    #null=True,blank=True
    ) #Создание ключа с сылкой на класс БД, типа FK, удаление

    def __str__(self):
        return '{} - {}'.format(self.fk_post,self.author)

    class Meta:
        verbose_name= 'Комментарий '
        verbose_name_plural='Комментарии'
        db_table = 'comment'
        permissions = (("can_see_author", "Можно видеть автора коментария."),)

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование тега')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def get_update_url(self):
        return reverse("tag_update_url", kwargs={"id_tag": self.pk})

    def get_delete_url(self):
        return reverse("tag_delete_url", kwargs={"id_tag": self.pk})

