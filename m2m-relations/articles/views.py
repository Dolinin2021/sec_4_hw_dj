from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    article_list = student_list = Article.objects.all()
    template = 'articles/news.html'
    context = {
        'object_list': article_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
