from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
from django.core.paginator import Paginator



def home(request):
    art = Article.objects.filter(status='p')[:5]

    context = {
        "art": art,
    }
    return render(request, 'index.html', context)



def about(request):
    art = Article.objects.filter(status='p')[:5]

    context = {
        "art": art,
    }
    return render(request, 'about.html', context)



def news(request, page=1):
    article_list = Article.objects.filter(status='p')
    paginator = Paginator(article_list, 6)
    articles = paginator.get_page(page)


    art = Article.objects.filter(status='p')[:5]


    context = {
        "articles": articles,
        "art":art,
    }
    return render(request, 'news.html', context)



def detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='p')

    art = Article.objects.filter(status='p')[:5]

    context = {
        "article": article,
        "art": art,
    }
    return render(request, "detail.html", context)



def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    
    return render(request,'error_404.html', data)
