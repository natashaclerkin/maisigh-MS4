from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blogs'),
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete/<slug:slug>/', views.delete_blog, name='delete_blog'),
]
