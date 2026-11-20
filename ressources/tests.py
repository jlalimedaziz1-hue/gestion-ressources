from django.test import TestCase
from django.urls import reverse
from .models import Categorie, Ressource


class RessourceTestCase(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(
            nom="Informatique",
            description="Catégorie informatique"
        )

        self.ressource = Ressource.objects.create(
            titre="Introduction Django",
            description="Cours Django",
            type_ressource="Cours",
            lien="https://www.djangoproject.com/",
            categorie=self.categorie
        )

    def test_creation_categorie(self):
        self.assertEqual(self.categorie.nom, "Informatique")

    def test_creation_ressource(self):
        self.assertEqual(
            self.ressource.titre,
            "Introduction Django"
        )

    def test_page_accueil(self):
        response = self.client.get(reverse('accueil'))
        self.assertEqual(response.status_code, 200)

    def test_liste_ressources(self):
        response = self.client.get(reverse('liste_ressources'))
        self.assertEqual(response.status_code, 200)

    def test_detail_ressource(self):
        response = self.client.get(
            reverse('detail_ressource', args=[self.ressource.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_liste_categories(self):
        response = self.client.get(reverse('liste_categories'))
        self.assertEqual(response.status_code, 200)

    def test_ressources_par_categorie(self):
        response = self.client.get(
            reverse('ressources_par_categorie', args=[self.categorie.id])
        )
        self.assertEqual(response.status_code, 200)