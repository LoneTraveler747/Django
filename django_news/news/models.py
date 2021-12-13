from django import db
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import Case
from django.shortcuts import render
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовк статьи')
    text = models.TextField(max_length=500,verbose_name='Текст')
    author = models.CharField(max_length=50,verbose_name='Автор')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',auto_now=True)

    class Meta:
        verbose_name= 'Статья '
        verbose_name_plural='Статьи'

    
    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"id_post": self.pk})

    
    def __str__(self):
         return self.title

class Comment(models.Model):
    text = models.TextField(max_length=500,verbose_name='Текст')
    author = models.CharField(max_length=50,verbose_name='Автор')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',auto_now=True)

    fk_post = models.ForeignKey(to=Post,on_delete=CASCADE,
    #null=True,blank=True
    ) #Создание ключа с сылкой на класс БД, типа FK, удаление

    def __str__(self):
        return '{} - {}'.format(self.fk_post,self.author)

    class Meta:
        verbose_name= 'Комментарий '
        verbose_name_plural='Комментарии'
        db_table = 'comment'