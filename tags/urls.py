from django.urls import path
from .views import TagPostListView, TagListView

urlpatterns = [
    path('', TagListView.as_view()),
    path('posts/', TagPostListView.as_view()),
]
