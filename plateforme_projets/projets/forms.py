from django import forms
from .models import Projet

class ProjetForm(forms.ModelForm):
    class meta:
        model = Projet
        fields = ['titre', 'description', 'filiere', 'pdf', 'image']