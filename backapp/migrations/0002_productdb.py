# Generated by Django 3.2.10 on 2023-06-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_names', models.CharField(blank=True, max_length=100, null=True)),
                ('Car_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Model', models.IntegerField(blank=True, null=True)),
                ('Hpower', models.IntegerField(blank=True, null=True)),
                ('Ceat', models.IntegerField(blank=True, null=True)),
                ('Body', models.IntegerField(blank=True, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
                ('Colour', models.CharField(blank=True, max_length=100, null=True)),
                ('Discription', models.CharField(blank=True, max_length=1000, null=True)),
                ('P_Image1', models.ImageField(blank=True, null=True, upload_to='product')),
            ],
        ),
    ]
