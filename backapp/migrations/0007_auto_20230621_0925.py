# Generated by Django 3.2.10 on 2023-06-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0006_auto_20230620_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='P_Image1',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='productdb',
            name='P_Image2',
            field=models.ImageField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='productdb',
            name='P_Image3',
            field=models.ImageField(upload_to='product'),
        ),
    ]