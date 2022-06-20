from django.shortcuts import render

from app01 import models


def index(request):
    all_article = models.Article.objects.all()
    return render(request, 'index_article_list.html', {
        'all_article': all_article
    })
