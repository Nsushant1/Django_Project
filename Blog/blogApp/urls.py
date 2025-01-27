from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/update/', views.update_blog, name='update_blog'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
]
