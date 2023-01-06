from django import  forms
from gestionimo.models import Locataire


class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire
        fields = '__all__'