from django.urls import path, include
from .views import PostViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]