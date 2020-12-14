from django.shortcuts import render

from rest_framework import generics

from .models import *
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateAPIView):
    serializer_class = PostSerializer
