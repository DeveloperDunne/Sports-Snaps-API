from django_filters.rest_framework import DjangoFilterBackend
from ss_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Categories

class CategoryList(generics.ListAPIView):
    queryset = Categories.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]