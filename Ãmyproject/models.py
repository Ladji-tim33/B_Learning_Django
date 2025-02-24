from django.db import models


class Article(models.Model):
    titre = models.CharField()
    contenu = models.TextField()
    date_publication = models.DateTimeField()