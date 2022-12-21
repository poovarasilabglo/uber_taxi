# Generated by Django 4.1.1 on 2022-12-17 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0004_alter_passenger_dropoff_location_and_more'),
        ('uber', '0007_driver_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passenger.passenger'),
        ),
    ]