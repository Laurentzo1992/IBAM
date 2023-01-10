from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from phone_field import PhoneField


class TypeLoyer(models.Model):
    libelle = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.libelle
        
        
class Loyer(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField()
    nbr_piece = models.IntegerField()
    adresse = models.TextField()
    type = models.ForeignKey(TypeLoyer, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class Locataire(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, verbose_name="Numero de téléphone", null=True)
    date_location = models.DateField(null=True)
    loue = models.ForeignKey(Loyer, null=True, on_delete=models.CASCADE, verbose_name="Loyé")
    
    
    def __str__(self):
        return self.nom
    
# Create your models here.
