from django.urls import path
from .views import CommentListCreateView

app_name = 'posts'

urlpatterns = [
    path('', CommentListCreateView.as_view(), name='list'),
]
