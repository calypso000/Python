from django.urls import path
from . import views

urlpatterns = [

    path('inscription',views.inscriptionPage,name='inscription'),
    path('connexion', views.connexionPage, name='connexion'),

]