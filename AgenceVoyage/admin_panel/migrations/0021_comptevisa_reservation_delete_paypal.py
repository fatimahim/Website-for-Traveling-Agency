# Generated by Django 5.0 on 2024-02-06 01:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0020_voyage_nombre_places'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteVisa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomComplet', models.CharField(max_length=200, unique=True)),
                ('cardNumber', models.CharField(max_length=200, unique=True)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('solde', models.DecimalField(decimal_places=2, max_digits=29)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nbDePlace', models.IntegerField(default=0)),
                ('nbDeChambre', models.IntegerField(default=0)),
                ('prixTotal', models.DecimalField(decimal_places=2, max_digits=29)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.voyage')),
            ],
        ),
        migrations.DeleteModel(
            name='PayPal',
        ),
    ]