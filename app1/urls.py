from django.urls import path



from .views import v_add_numbers, v_add_numbers2
from . import views

urlpatterns = [

   

    path('add2/', v_add_numbers2, name='n_add_numbers2'),

    path('add/', v_add_numbers, name='n_add_numbers'),
    
    path('', views.liste_etudiants, name='liste_etudiants'),


    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),

    path('modifier/<int:pk>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('supprimer/<int:pk>/', views.supprimer_etudiant, name='supprimer_etudiant'),

]
