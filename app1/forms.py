# forms.py
from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        #han diro wch 3ndkom column 
        fields = ['nom', 'prenom', 'matricule']
        #hadi partie bah diro css t9dro mdirohach 
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
        }

