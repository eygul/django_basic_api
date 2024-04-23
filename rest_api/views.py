from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
#class based views
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins

class genericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)
        
