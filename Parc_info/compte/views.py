from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreerUtilisateur


# Create your views here.
def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
    if form.is_valid():
        form.save()
        user=form.cleaned_data.get('usename')
        messages.success(request,'compte creer avec succes')
        return redirect('connexion')
    context={'form':form}
    return render(request,'compte/inscription.html', context)

def connexionPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        use=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request,"Veuillez essayer a nouveau")
    return render(request,'compte/connexion.html', context)