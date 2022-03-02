from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    article_list = Article.objects.all().order_by(ordering)
    template = 'articles/news.html'
    context = {
        'object_list': article_list
    }
    return render(request, template, context)