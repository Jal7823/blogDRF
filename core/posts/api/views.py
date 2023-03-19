from rest_framework import viewsets,status
from rest_framework.response import Response

from ..models import Category,Post
from .serializer import SerializerCategories,SerializerPost


class ViewSetPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = SerializerPost


class ViewSetCategories(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SerializerCategories