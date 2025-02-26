from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.PostApiView.as_view(), name='list'),
    path('posts/<int:pk>/', views.PostDetailApiView.as_view(), name='detail'),
]
