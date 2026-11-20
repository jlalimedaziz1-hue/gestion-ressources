from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Ressource(models.Model):
    TYPES = [
        ('Cours', 'Cours'),
        ('Tutoriel', 'Tutoriel'),
        ('Vidéo', 'Vidéo'),
        ('Exercice', 'Exercice'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    type_ressource = models.CharField(max_length=20, choices=TYPES)
    lien = models.URLField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre