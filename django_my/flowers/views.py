from django.shortcuts import render
from .models import Articles

def home(request):
    return render(request,'flowers/home.html')

def pions(request):
    return render(request,'flowers/pions.html')

def Articles(request):
    flowers = Articles.objects.all()  # Получить все объекты Articles из базы данных
    return render(request, 'flowers/pions.html', {'flowers': flowers})
