from django.shortcuts import render, get_object_or_404
from . import models

def blogs_view(request):
    if request.method == "GET":
        blogs = models.Blog_post.objects.all().order_by('-id')
        news = models.News.objects.all().order_by('-id')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs, 'news': news})

def blog_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(models.Blog_post, id = id)
    return render(request, "blogs/blog_detail.html", {'blog_id': blog_id})


def project_description(request):
    if request.method == 'GET':
        description = {
            'title': 'Math forum',
            'info': '''The aim of this project is to create a math forum''',
            'features': ['Creation of blogs', 'Discussion of topics', 'Edutorials'],
            'topics': ['Number Theory', 'Geometry', 'Algebra', 'Combinatorics']
        }
    return render(request, 'description.html', description)

def about_me(request):
    if request.method == 'GET':
        info = {
            'name': 'Aziret Akmatbek uulu',
            'age': 21,
            'interests': ["Math", "Table Tennis", "Programming", "Leathercrafting"]
        }
    return render(request, 'about_me.html', info)