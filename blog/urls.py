from django.urls import path
from . import views

urlpatterns = [
    path('description/', views.project_description, name = 'description'),
    path('about_me/', views.about_me, name = 'about_me'),
    path('blog_list/', views.blogs_view, name = 'blog_list'),
    path('blog_list/<int:id>/', views.blog_detail_view, name = 'blog_detail'),
]
