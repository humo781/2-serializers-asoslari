from rest_framework.generics import ListAPIView
from .models import Category
from .serializers import CategorySerializer, CategoryPostSerializer


class CategoryPostListView(ListAPIView):
    queryset = Category.objects.prefetch_related('posts').all()
    serializer_class = CategoryPostSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
