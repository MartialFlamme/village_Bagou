from django.shortcuts import render

def liste_projets(request):
    projets = [
        {'titre': 'Forage d’eau potable à Lafeng', 'etat': 'En cours', 'image': 'images/projets/forage.jpg'},
        {'titre': 'Réhabilitation de l’école primaire', 'etat': 'Terminé', 'image': 'images/projets/ecole.jpg'},
    ]
    return render(request, 'projets/liste_projets.html', {'projets': projets})

def detail_projet(request):
    projet = {
        'titre': 'Forage d’eau potable à Lafeng',
        'etat': 'En cours',
        'description': """
            Ce projet vise à doter le quartier Lafeng d’un forage moderne permettant l’accès à l’eau potable
            pour plus de 600 habitants. Il est soutenu par la Fondation Gacha et des donateurs de la diaspora.
        """,
        'partenaires': ['Fondation Gacha', 'CODEBA', 'Diaspora Europe'],
        'image': 'images/projets/forage.jpg'
    }
    return render(request, 'projets/detail_projet.html', {'projet': projet})
