from django import  forms
from gestionimo.models import Locataire
from django.core.validators import RegexValidator
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget


class LocataireForm(forms.ModelForm):
    
    date_location = forms.DateField(
        label='Date de location',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    nom = forms.CharField(
        label='Nom', min_length=2, max_length=100,
        validators=[RegexValidator(r'^[A-Z0-9]*$',
        message="Lettre majuscule et chiffre autorisé")],
        widget=forms.TextInput(attrs={'placeholder': 'Nom'})
    )
    
    prenom = forms.CharField(
        label='Prenom', min_length=2, max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Prenom'})
    )
    
    
    age = forms.CharField(
        label='Age', min_length=1, max_length=3,
        validators=[RegexValidator(r'^[0-9]*$',
        message="Chiffre autorisé uniquement ")],
        widget=forms.TextInput(attrs={'placeholder': 'Age'})
    )

    
    class Meta:
        model = Locataire
        fields = '__all__'
        
        widgets = {
            'phone_number': PhoneNumberPrefixWidget,
        }
                    
