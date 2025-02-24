from django.urls import path 
from . import views

urlpatterns = [
    path('creer/', views.create_article, name="creer_article"),
    path('', views.page_accueil, name="page_accueil"),
    path('article/<int:id>/', views.afficher_article, name="afficher_article"), 
]
