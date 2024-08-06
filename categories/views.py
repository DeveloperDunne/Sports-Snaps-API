from django_filters.rest_framework import DjangoFilterBackend
from ss_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]