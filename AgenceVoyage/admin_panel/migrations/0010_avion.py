# Generated by Django 5.0 on 2024-02-02 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_panel", "0009_delete_avion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nomAvion", models.CharField(max_length=200)),
                ("villeDepart", models.CharField(max_length=200)),
                ("dateDepart", models.DateField()),
                ("dateRetour", models.DateField()),
                ("prix", models.DecimalField(decimal_places=2, max_digits=18)),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_panel.destination",
                    ),
                ),
            ],
        ),
    ]