# Generated by Django 5.0 on 2024-02-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_panel", "0019_comptepaypal_paypal_remove_voyage_nombre_places"),
    ]

    operations = [
        migrations.AddField(
            model_name="voyage",
            name="nombre_places",
            field=models.IntegerField(default=0),
        ),
    ]