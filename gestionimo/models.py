from django.db import models

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
    age = models.IntegerField()
    loue = models.ForeignKey(Loyer, null=True, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.nom
    
# Create your models here.
