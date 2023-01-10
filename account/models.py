# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    
    ROLE = [(ADMIN, 'Admin'),(CUSTOMER, 'Customer'),]
    
    profile_photo = models.ImageField(upload_to='uploads_images/', verbose_name='Photo de profil', null=True, blank=True, default='uploads_images/img.png')
    role = models.CharField(max_length=30, choices=ROLE, verbose_name='Rôle', null=True, blank=True)
    
    @property
    def profile_photoURL(self):
        try:
            url = self.profile_photo.url
        except:
            url = ''
        return url