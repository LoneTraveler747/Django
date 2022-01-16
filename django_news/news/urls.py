from django.urls import path
from . import views

urlpatterns = [
    path('list_posts/', views.index, name='list_posts_url'),
    
    path('<int:id_post>', views.post_detail, name='post_detail_url'),

    path('post/<int:id_post>/add_comment', views.add_comment, name='add_comment_url'), #Новое

    path('tags/', views.tags_list, name = 'tags_list_url')
]
