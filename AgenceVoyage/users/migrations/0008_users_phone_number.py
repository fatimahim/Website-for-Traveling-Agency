# Generated by Django 5.0 on 2023-12-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_customuser_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]