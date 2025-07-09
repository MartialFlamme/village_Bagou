from django.urls import path
from . import views

app_name = 'associations'

urlpatterns = [
    path('', views.liste_associations, name='liste'),
    path('detail/<slug:slug>/', views.detail_association, name='detail'),
]
