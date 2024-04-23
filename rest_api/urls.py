from django.urls import path
from .views import genericAPIView

urlpatterns = [
    path('posts/<int:id>/', genericAPIView.as_view())
]