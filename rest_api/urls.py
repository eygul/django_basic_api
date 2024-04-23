from django.urls import path
from .views import PostsView, PostDetail

urlpatterns = [
    path('posts/', PostsView.as_view()),
    path('details/<int:pk>', PostDetail.as_view()),
]