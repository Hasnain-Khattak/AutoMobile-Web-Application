# Generated by Django 5.0.4 on 2024-04-30 06:22

import django.db.models.deletion
import localflavor.pk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=localflavor.pk.models.PKStateField(default='PK-KP', max_length=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=localflavor.pk.models.PKPostCodeField(blank=True, max_length=5),
        ),
    ]
