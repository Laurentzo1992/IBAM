# Generated by Django 3.2.5 on 2023-01-10 01:06

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionimo', '0003_locataire_phone_number2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locataire',
            name='phone_number2',
            field=phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Numero de téléphone'),
        ),
    ]
