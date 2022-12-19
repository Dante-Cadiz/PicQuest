from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('create_post/', views.AddPost, name='create_post'),
    path('your_posts/', views.YourPosts.as_view(), name='your_posts'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]