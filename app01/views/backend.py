from django.shortcuts import render, redirect

from app01 import models
from app01.views.forms import ArticleForm, ArticleDetailForm


def backend(request):
    return render(request, 'dashboard.html')


def article_list(request):
    all_article = models.Article.objects.filter(delete_status=0, author=request.my_user)

    return render(request, 'user_article_list.html', {
        'all_article': all_article
    })


def article_add(request):
    obj = models.Article(author=request.my_user)
    form_obj = ArticleForm(instance=obj)
    article_detail_obj = ArticleDetailForm()
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST, instance=obj)
        article_detail_obj = ArticleDetailForm(request.POST)

        if form_obj.is_valid() and article_detail_obj.is_valid():
            detail_obj = article_detail_obj.save()
            form_obj.instance.detail_id = detail_obj.pk
            form_obj.save()
            return redirect('article_list')
    return render(request, 'article_add.html', {
        'form_obj': form_obj,
        'article_detail_obj': article_detail_obj
    })


def article_edit(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()
    form_obj = ArticleForm(instance=obj)
    article_detail_obj = ArticleDetailForm(instance=obj.detail)

    if request.method == 'POST':
        form_obj = ArticleForm(request.POST, instance=obj)
        article_detail_obj = ArticleDetailForm(request.POST, instance=obj.detail)

        if form_obj.is_valid() and article_detail_obj.is_valid():
            detail_obj = article_detail_obj.save()
            form_obj.instance.detail_id = detail_obj.pk
            form_obj.save()
            return redirect('article_list')
    return render(request, 'article_edit.html', {
        'form_obj': form_obj,
        'article_detail_obj': article_detail_obj
    })


def article_delete(request, pk):
    obj = models.Article.objects.filter(pk=pk).first()
    obj.delete_status = True
    obj.save()
    return redirect('article_list')
