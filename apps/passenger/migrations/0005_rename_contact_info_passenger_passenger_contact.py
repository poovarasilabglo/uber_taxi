# Generated by Django 4.1.1 on 2022-12-19 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0004_alter_passenger_dropoff_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='contact_info',
            new_name='passenger_contact',
        ),
    ]
