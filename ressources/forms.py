
from django import forms
from .models import Ressource


class RessourceForm(forms.ModelForm):

    class Meta:
        model = Ressource
        fields = [
            'titre',
            'description',
            'type_ressource',
            'lien',
            'categorie',
        ]
