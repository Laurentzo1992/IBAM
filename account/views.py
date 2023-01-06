# account/views.py
from django.conf import settings
from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login, authenticate, logout, get_user_model
User = get_user_model()

def login_page(request):
    #crée une instance du formulaire
    form = forms.LoginForm()
    #definir une variable message pour informer le user si ses identifiant sont iccorecte
    message = ''
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.LoginForm(request.POST)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #On authentifie l'instance du user avec la methode authenticate
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            #Test si le usernme  envoyé du fomrulair ,'est pas null
            if user is not None:
                #Etablie une connection de lutilisateur
                login(request, user)
                #On le redirige vers une page ici c'est index.html
                return redirect('index')
            #si le formulaire n'est pas correct e.i si des les données dont incorrecte informé le user
        message = 'Identifiants invalides.'
    return render(request, 'account/login.html', context={'form': form, 'message': message})




def logout_user(request):
    #deconnection du user avec la methode logout 
    logout(request)
    return redirect('login_page')



def register(request):
    #crée une instance du formulaire
    form = forms.RegisterForm()
    #Test l'action si post (envoi de donnée)
    if request.method == 'POST':
        # On recupère les données dans l'instance du formulaire
        form = forms.RegisterForm(request.POST, request.FILES)
        #Verifie si le formulaire est valide
        if form.is_valid():
            #sauvegarde
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'account/register.html', context={'form': form})



def users(request):
    user_all = User.objects.all()
    return render(request, 'account/users.html', {"user_all":user_all})