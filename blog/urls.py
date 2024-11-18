from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
]
