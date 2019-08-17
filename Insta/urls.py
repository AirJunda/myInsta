"""day1up URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from Insta.views import HelloWorld
from Insta.views import (PostsView, PostDetailView, PostCreatView,PostUpdateView, 
                         PostDeleteView, SignUp, addLike, UserDetailView,addComment,toggleFollow,UserUpdateView,
                         FollowingPostsView, FollowingUserView, FollowerView                      
                         )

urlpatterns = [
    path('helloworld', HelloWorld.as_view(),name='home'),
    path('', PostsView.as_view(),name='posts'),
    path('followingPosts', FollowingPostsView.as_view(),name='following_posts'),
    path('post/<int:pk>', PostDetailView.as_view(),name='post_detail'),
    path('post/new/', PostCreatView.as_view(),name='make_post'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(),name='edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(),name='delete_post'),
    path('arthr/signup', SignUp.as_view(),name='signup'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('comment', addComment, name='addComment'),
    path('togglefollow', toggleFollow, name='togglefollow'),   #处理关注和取关
    path('user/edit_profile/<int:pk>/', UserUpdateView.as_view(), name='edit_profile'),   #处理edit profile
    path('follower', FollowerView.as_view(), name='follower'),
    path('following', FollowingUserView.as_view(), name='following'),   #处理显示关注的users



]
