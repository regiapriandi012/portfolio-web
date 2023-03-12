from django.shortcuts import render
from .models import Github, Article

# Create your views here.
def index(request):
    github = Github.objects.all()
    article = Article.objects.all()
    context = {
        'githubs': github,
        'articles': article,
        'github_topics': " ".join([p.topics for p in github]).split(", "),
        'article_topics': " ".join([p.topics for p in article]).split(", "),
    }
    return render(request, 'webfortoapp/index.html', context)
