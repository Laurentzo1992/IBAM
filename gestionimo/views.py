from django.shortcuts import render, redirect
from gestionimo.models import Locataire
from gestionimo.forms import LocataireForm
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required
def index(request):
    #Recupéré et affiché les données
    locataires = Locataire.objects.all()
    paginator = Paginator(locataires, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gestionimo/index.html', {"page_obj":page_obj})

@login_required
def create_locataire(request):
    # test Si la request est une soumission
    if request.method == 'POST':
        #On initialise le formulaire avec les données contenues
        form = LocataireForm(request.POST)
        #test si le formulaire est valide 
        if form.is_valid():
            #On enregistre
            form.save()
            return redirect("index")
    else:
        #si non on initialise un formualire vide
        form = LocataireForm()
    return render(request, 'gestionimo/create_locataire.html', {"form":form})

@login_required
def update(request, id):
    locataire = Locataire.objects.get(id=id)
    if request.method == 'POST':
        form = LocataireForm(request.POST, instance=locataire)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"successfully {locataire.nom} was edited !")
            return redirect('index')
    else:
        form = LocataireForm(instance=locataire)
    return render(request, 'gestionimo/update.html', {'form':form})


@login_required
def delete(request, id):
    locataire = Locataire.objects.get(id=id)
    if request.method=='POST':
        locataire.delete()
        messages.success(request, f'{locataire.nom} deleted successfully !')
        return redirect("index")
    return render(request, 'gestionimo/delete.html', {"locataire":locataire})



# Create your views here.
