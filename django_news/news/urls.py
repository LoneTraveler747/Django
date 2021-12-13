from django.urls import path
from . import views

urlpatterns = [
    path('list_posts', views.index, name='list_posts_url'),

    path('<int:id_post>', views.post_detail, name='post_detail_url')
]
