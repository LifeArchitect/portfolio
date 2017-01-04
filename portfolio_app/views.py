from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def experiences(request, id):
    return render(request, 'experiences.html', {})

def assignment1(request):
    return render(request, 'assignment1.html', {})
