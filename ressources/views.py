
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categorie, Ressource
from .forms import RessourceForm


# Page d'accueil
def accueil(request):
    categories = Categorie.objects.all()
    ressources = Ressource.objects.all()

    return render(request, 'ressources/accueil.html', {
        'categories': categories,
        'ressources': ressources,
    })


# Liste des ressources
def liste_ressources(request):
    ressources = Ressource.objects.all()

    return render(request, 'ressources/liste_ressources.html', {
        'ressources': ressources
    })


# Detail d'une ressource
def detail_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    return render(request, 'ressources/detail_ressource.html', {
        'ressource': ressource
    })


# Ajouter une ressource
def ajouter_ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Ressource ajoutée avec succès.')
            return redirect('liste_ressources')
    else:
        form = RessourceForm()

    return render(request, 'ressources/formulaire_ressource.html', {
        'form': form
    })
# Modifier une ressource
def modifier_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    if request.method == 'POST':
        form = RessourceForm(request.POST, instance=ressource)

        if form.is_valid():
            form.save()
            messages.success(request, 'Ressource modifiée avec succès.')
            return redirect('liste_ressources')
    else:
        form = RessourceForm(instance=ressource)

    return render(request, 'ressources/formulaire_ressource.html', {
        'form': form
    })
# Supprimer une ressource
def supprimer_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    if request.method == 'POST':
        ressource.delete()
        messages.success(request, 'Ressource supprimée avec succès.')
        return redirect('liste_ressources')

    return render(request, 'ressources/supprimer_ressource.html', {
        'ressource': ressource
    })
    # Liste des categories
def liste_categories(request):
    categories = Categorie.objects.all()

    return render(request, 'ressources/liste_categories.html', {
        'categories': categories
    })


# Ressources par categorie
def ressources_par_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    ressources = Ressource.objects.filter(categorie=categorie)

    return render(request, 'ressources/ressources_categorie.html', {
        'categorie': categorie,
        'ressources': ressources
    })