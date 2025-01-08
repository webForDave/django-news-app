from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles


class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'