from django.urls import path
from . import views

urlpatterns = [

    path('inscription',views.inscriptionPage,name='inscription'),
    path('Connexion', views.connexionPage, name='Connexion'),

]