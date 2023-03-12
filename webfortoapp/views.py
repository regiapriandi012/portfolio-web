from django.shortcuts import render
from .models import Github, Article

# Create your views here.
def index(request):
    github = Github.objects.all()
    article = Article.objects.all()

    context = {
        'githubs': github,
        'aricles': article,
    }
    return render(request, 'webfortoapp/index.html', context)
