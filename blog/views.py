from django.shortcuts import render

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