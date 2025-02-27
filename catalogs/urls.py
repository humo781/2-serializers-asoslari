from django.urls import path
from .views import CategoryListView, CategoryPostListView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('posts/', CategoryPostListView.as_view()),
]
