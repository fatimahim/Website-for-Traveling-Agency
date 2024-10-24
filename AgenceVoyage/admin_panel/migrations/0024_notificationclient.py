# Generated by Django 5.0 on 2024-02-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_panel", "0023_promotion"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationClient",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.CharField(default="", max_length=800)),
                ("voyage", models.CharField(default="", max_length=800)),
            ],
        ),
    ]