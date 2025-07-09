from django.shortcuts import render, get_object_or_404
from .models import Association

def liste_associations(request):
    associations = Association.objects.all()
    return render(request, 'associations/liste_associations.html', {'associations': associations})

def detail_association(request, slug):
    association = get_object_or_404(Association, slug=slug)
    return render(request, 'associations/detail_association.html', {'association': association})
