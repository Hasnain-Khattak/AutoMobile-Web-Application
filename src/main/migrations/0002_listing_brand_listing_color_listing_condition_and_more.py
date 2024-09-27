# Generated by Django 5.0.4 on 2024-05-03 11:31

import django.db.models.deletion
import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0006_alter_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('samsung', 'Samsung Galaxy'), ('vivo', 'Vivo'), ('realme', 'Realme'), ('huawei', 'Huawei'), ('xiaomi', 'Xiaomi'), ('infinix', 'Infinix'), ('oneplus', 'OnePlus'), ('oppo', 'Oppo'), ('nokia', 'Nokia'), ('sony', 'Sony'), ('apple', 'Apple'), ('techSpark', 'TechSPARK'), ('asus', 'Asus'), ('tecno', 'Tecno'), ('redmi', 'Redmi'), ('google-mobile', 'Google Mobile'), ('blackberry', 'Blackberry'), ('qmobile', 'QMobile'), ('motorola', 'Motorola'), ('htc', 'HTC'), ('lenovo', 'Lenovo'), ('lava', 'Lava'), ('lg', 'LG'), ('poco', 'Poco'), ('micromax', 'Micromax'), ('other', 'Other')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished'), ('damaged', 'Damaged'), ('broken', 'Broken'), ('other', 'Other')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default=None, upload_to=main.utils.user_listing_path),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
