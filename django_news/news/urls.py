from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('list_posts/', views.index, name='list_posts_url'),

    path('post_create', views.PostCreate.as_view(), name= 'post_create_url'), #Добалвение постов
    
    path('<int:id_post>', views.post_detail, name='post_detail_url'),

    path('post/<int:id_post>/add_comment', views.add_comment, name='add_comment_url'), #Новое

    path('tags/', views.tags_list, name = 'tags_list_url'),
    
    path('tag_create', views.TagCreate.as_view(), name='tag_create_url'),

    path('<int:id_post>/post_update/', views.PostUpdate.as_view(), name="post_update_url"),

    path('<int:id_post>/post_delete/', views.PostDelete.as_view(), name= "post_delete_url"),
]
