from django.shortcuts import render

def projets_educatifs(request):
    projets = [
        {'titre': 'Ateliers numériques pour les jeunes', 'description': 'Initiation à l’informatique et à Internet dans les écoles.'},
        {'titre': 'Éducation civique communautaire', 'description': 'Formations sur la citoyenneté et l’engagement local.'},
    ]
    return render(request, 'education/projets_educatifs.html', {'projets': projets})

def academie_hoteliere(request):
    contenu = {
        'nom': 'Académie Hôtelière de Bangoulap',
        'description': """
            Ce centre de formation vise à préparer les jeunes aux métiers de l’hôtellerie, de la restauration
            et du tourisme rural, en valorisant les produits et coutumes locales.
        """,
        'image': 'images/education/academie.jpg'
    }
    return render(request, 'education/academie_hoteliere.html', {'contenu': contenu})

def infrastructures(request):
    infrastructures = [
        {'type': 'Route rurale', 'image': 'images/education/route.jpg', 'description': 'Route reliant Bangoulap au marché régional.'},
        {'type': 'École primaire', 'image': 'images/education/ecole.jpg', 'description': 'Rénovation des salles de classe et dotation en manuels.'},
        {'type': 'Forage d’eau', 'image': 'images/education/forage.jpg', 'description': 'Accès à l’eau potable dans le quartier Lafeng.'},
    ]
    return render(request, 'education/infrastructures.html', {'infrastructures': infrastructures})
