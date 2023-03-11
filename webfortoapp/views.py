from django.shortcuts import render
from .models import Github, Article, Certificate

# Create your views here.
def index(request):
    github = Github.objects.all()
    article = Article.objects.all()
    certificate = Certificate.objects.all()

    context = {
        'githubs': github,
        'aricles': article,
        'certificates': certificate,
    }
    return render(request, 'webfortoapp/index.html', context)