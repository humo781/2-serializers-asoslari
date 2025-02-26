from rest_framework.generics import ListCreateAPIView
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.filter(parent_comment=None)
    serializer_class = CommentSerializer
