# Generated by Django 4.1.1 on 2022-12-17 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0003_remove_passenger_locations_and_more'),
        ('uber', '0005_alter_driver_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='passenger_location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
