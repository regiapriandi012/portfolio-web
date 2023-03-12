from django.contrib import admin
from .models import *

# Register your models here.
class GithubAdmin(admin.ModelAdmin):
    list_display = ('repo_name', 'programming_language', 'created_at', 'updated_at')
    list_filter = ("repo_name",)
    search_fields = ['repo_name', 'programming_language', 'created_at', 'updated_at']
    prepopulated_fields = {'repo_name': ('repo_name',)}
admin.site.register(Github, GithubAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ("title",)
    list_filter = ("title",)
    search_fields = ['title', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'title': ('title',)}
admin.site.register(Article, ArticleAdmin)
