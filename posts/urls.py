from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostApiView.as_view()),
    path('<int:pk>/', views.PostDetailApiView.as_view()),
]
