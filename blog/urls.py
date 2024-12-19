from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name = "blog-index"),
    path("post/<int:pk>/", views.blog_detail, name="blog-detail"),
    path("category/<category>", views.blog_category, name = "blog-category"),
]
