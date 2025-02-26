from django.urls import path
from .views import CategoryListView

app_name = 'catalogs'
urlpatterns = [
    path('get/', CategoryListView.as_view(), name='list'),
]
