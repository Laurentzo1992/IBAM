# Generated by Django 3.2.5 on 2023-01-05 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeLoyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('price', models.FloatField()),
                ('nbr_piece', models.IntegerField()),
                ('adresse', models.TextField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionimo.typeloyer')),
            ],
        ),
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('loue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionimo.loyer')),
            ],
        ),
    ]
