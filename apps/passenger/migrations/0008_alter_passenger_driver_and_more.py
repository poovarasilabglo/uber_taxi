# Generated by Django 4.1.1 on 2022-12-20 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0016_alter_driver_car_brand_alter_driver_number_plate_and_more'),
        ('passenger', '0007_passenger_driver_passenger_dropoff_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.driver'),
        ),
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
