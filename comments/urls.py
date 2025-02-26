from django.urls import path
from .views import CommentListCreateView

app_name = 'posts'

urlpatterns = [
    path('posts/', CommentListCreateView.as_view(), name='list'),
]
