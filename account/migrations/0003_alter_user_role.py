# Generated by Django 3.2.5 on 2023-01-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'Customer')], max_length=30, null=True, verbose_name='Rôle'),
        ),
    ]
