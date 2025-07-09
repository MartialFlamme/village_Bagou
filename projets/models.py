from django.db import models

class Projet(models.Model):
    ETATS = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('a_venir', 'À venir'),
    ]

    nom = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/')
    etat = models.CharField(max_length=20, choices=ETATS, default='en_cours')
    partenaires = models.TextField(help_text="Séparer les noms par des virgules")

    def __str__(self):
        return self.nom
