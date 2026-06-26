from django.urls import path
from . import views

urlpatterns = [
    path('description/', views.project_description, name = 'description'),
    path('about_me/', views.about_me, name = 'about me')
]
