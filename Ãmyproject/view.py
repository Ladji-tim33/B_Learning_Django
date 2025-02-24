from django.shortcuts import render
from .models import Article



def afficher_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})