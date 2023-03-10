# Generated by Django 4.1.1 on 2022-12-15 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=50)),
                ('number_plate', models.CharField(max_length=20)),
                ('seat_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=100)),
                ('dropoff_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('bio', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profilepicture/')),
                ('contact_info', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[(1, 'Requested'), (2, 'Started'), (3, 'In_Progress'), (4, 'Completed')], default=1, max_length=100)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('passenger_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.location')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
