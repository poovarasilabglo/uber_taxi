# Generated by Django 4.1.1 on 2022-12-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]
