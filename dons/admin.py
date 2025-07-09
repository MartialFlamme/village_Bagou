from django.contrib import admin
from .models import Don

@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'montant', 'moyen', 'date')
    list_filter = ('moyen', 'date')
    search_fields = ('nom', 'email')
