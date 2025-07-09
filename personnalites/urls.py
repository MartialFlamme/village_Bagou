from django.urls import path
from . import views

app_name = "personnalites"

urlpatterns = [
    path('', views.liste_personnalites, name='liste'),
    path('<slug:slug>/', views.detail_personnalite, name='detail'),
]
