from django.shortcuts import render

from app01 import models


def article(request, pk):
    article_obj = models.Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {
        'article_obj': article_obj

    })
