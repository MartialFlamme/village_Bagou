from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etat', 'partenaires')
    search_fields = ('nom', 'etat', 'partenaires')
    list_filter = ('etat',)
