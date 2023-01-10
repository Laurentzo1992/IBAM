from django.contrib import admin
from gestionimo.models import Locataire, Loyer, TypeLoyer



class LocataireAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'prenom', 'email', 'phone_number', 'loue', 'date_location')
    search_fields = ['nom', 'prenom', 'phone_number', 'email']
    list_filter = ['nom', 'prenom', 'phone_number']
    list_per_page = 4
    
    
    



admin.site.register(Locataire, LocataireAdmin)
admin.site.register(Loyer)
admin.site.register(TypeLoyer)



    
