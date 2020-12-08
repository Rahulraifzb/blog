from django.urls import path, include
from .views import (
    home,
    about,
    DetailPost,
    CreatePost,
    UpdatePost,
    DeletePost,
    UserPostListView


)
urlpatterns = [
    path('', include('users.urls')),

    path('', home, name="home"),

    path('about/', about, name="about"),

    path('user/<str:username>/', UserPostListView.as_view(), name="user_post"),

    path('post/new/', CreatePost.as_view(),
         name="create_post"),

    path('post/<str:pk>/update/', UpdatePost.as_view(),
         name="update_post"),

    path('post/<str:pk>/delete/', DeletePost.as_view(),
         name="delete_post"),

    path('post/<str:pk>/', DetailPost.as_view(),
         name="detail_post"),



]
