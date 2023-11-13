from django.shortcuts import render, get_object_or_404
from .models import Articles
from .models import orchids

def home(request):
    return render(request,'flowers/home.html')



def ArticlesClass(request):
    flower = Articles.objects.all()
    return render(request, 'flowers/pions.html', {'flowers': flower})


def article_detail(request, article_id):
    flower = get_object_or_404(Articles, pk=article_id)
    return render(request, 'flowers/article_detail.html', {'flowers': flower})

def orchids_view(request):
    flower = orchids.objects.all()
    return render(request, 'flowers/orchids.html', {'flowers': flower})