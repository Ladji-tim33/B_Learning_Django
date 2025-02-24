from .forms import ArticleForm  # Correction de l'importation
from .models import Article
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def create_article(request):
    if request.method == 'POST':  # Correction de "methode"
        form = ArticleForm(request.POST)  # Correction de "from" -> "form"
        if form.is_valid():
            form.save()
            messages.success(request, "L'article a été créé avec succès")
            return redirect('page_accueil')
    else:
        form = ArticleForm()        

    return render(request, 'blog/creer_article.html', {'form': form})  # Correction du nom de la variable

def page_accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/page_accueil.html', {'articles': articles})  # Correction d'indentation

class ListeArticleView(ListView):
    model = Article  # Correction de "models" -> "model"
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'

def afficher_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/afficher_article.html', {'article': article})
