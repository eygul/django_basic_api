from django.urls import path, include
from .views import PostGenericViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('posts', PostGenericViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]