# Generated by Django 4.1.1 on 2022-12-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0002_remove_driver_created_on_remove_driver_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
