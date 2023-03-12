from django.db import models

# Create your models here.
class Github(models.Model):
    repo_name = models.CharField(max_length=200)
    topics = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    repo_url = models.URLField(max_length=100)
    user_url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.repo_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    topics = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    html_url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
