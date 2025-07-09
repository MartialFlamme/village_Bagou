from django.db import models
from projets.models import Projet  # ⚠️ Assure-toi que l'app "projets" est bien installée
from django.utils import timezone

class Don(models.Model):
    MOYENS = [
        ('momo', 'Mobile Money'),
        ('om', 'Orange Money'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    moyen = models.CharField(max_length=10, choices=MOYENS)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.montant} FCFA pour {self.projet.nom}"
