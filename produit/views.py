from django.http import HttpResponse
from django.shortcuts import render
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'Commandes':commandes,'Clients':clients }
    return render(request, 'produit/acceuil.html',context)
