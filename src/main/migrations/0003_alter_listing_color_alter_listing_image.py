# Generated by Django 5.0.4 on 2024-05-03 11:32

import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_listing_brand_listing_color_listing_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='color',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to=main.utils.user_listing_path),
        ),
    ]
