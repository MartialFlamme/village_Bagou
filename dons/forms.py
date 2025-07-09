from django import forms
from .models import Don

class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ['nom', 'email', 'numero', 'montant', 'moyen', 'projet']
