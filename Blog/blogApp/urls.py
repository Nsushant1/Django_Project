from django.urls import path
from .views import (
    blog_list, 
    create_blog, 
    update_blog, 
    delete_blog, 
    signup_view
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Blog URLs
    path('', blog_list, name='blog_list'),
    path('create/', create_blog, name='create_blog'),
    path('update/<int:blog_id>/', update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', delete_blog, name='delete_blog'),
 # Authentication URLs
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  
]
