# Generated by Django 3.2.10 on 2023-06-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0005_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Airbag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdb',
            name='P_Image2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='P_Image3',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Transmission',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]