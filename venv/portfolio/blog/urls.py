from django.urls import path
from .views import BlogListView, BlogView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/<slug:title>',  BlogView.as_view(), name='blog')
]
