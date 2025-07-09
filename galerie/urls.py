from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'galerie'

urlpatterns = [
    path('', RedirectView.as_view(url='photos/')),  # ✅ redirection vers la page par défaut
    path('photos/', views.photos, name='photos'),
    path('videos/', views.videos, name='videos'),
]
