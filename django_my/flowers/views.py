from django.shortcuts import render
from .models import Articles

def home(request):
    return render(request,'flowers/home.html')

# def pions(request):
#     return render(request,'flowers/pions.html')

def ArticlesClass(request):
    flower = Articles.objects.all()
    return render(request, 'flowers/pions.html', {'flowers': flower})
