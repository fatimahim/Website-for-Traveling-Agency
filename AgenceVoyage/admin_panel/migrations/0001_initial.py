# Generated by Django 5.0 on 2023-12-28 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ville', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.categorie')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.country')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hotelNom', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avionNom', models.CharField(max_length=200)),
                ('dateDepart', models.DateField()),
                ('dateRetour', models.DateField()),
                ('countryDepart', models.CharField(max_length=200)),
                ('villeDepart', models.CharField(max_length=200)),
                ('classe', models.CharField(max_length=10)),
                ('countryDestination', models.CharField(max_length=200)),
                ('villeDestination', models.CharField(max_length=200)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.voyage')),
            ],
        ),
    ]
