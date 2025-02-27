from rest_framework.generics import ListAPIView
from .models import Tag
from .serializers import TagSerializer, TagPostSerializer


class TagPostListView(ListAPIView):
    queryset = Tag.objects.prefetch_related('posts').all()
    serializer_class = TagPostSerializer

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
