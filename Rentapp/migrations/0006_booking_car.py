# Generated by Django 3.2.10 on 2023-06-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentapp', '0005_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Car',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
