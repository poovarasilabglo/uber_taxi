# Generated by Django 4.1.1 on 2022-12-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0003_remove_passenger_locations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='dropoff_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='pickup_location',
            field=models.CharField(max_length=100),
        ),
    ]
