from django.shortcuts import render

from rest_framework import generics

from .models import *
from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    serializer_class = PostSerializer
