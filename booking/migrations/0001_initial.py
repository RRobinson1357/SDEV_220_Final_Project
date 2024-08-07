# Generated by Django 5.0.2 on 2024-07-08 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('window_number', models.CharField(max_length=2)),
                ('bed_number', models.CharField(max_length=1)),
                ('sq_ft', models.CharField(max_length=4)),
                ('occupants', models.CharField(max_length=2)),
                ('room_desc', models.CharField(choices=[('Basic', 'desc'), ('Standard', 'desc'), ('Studio', 'desc')], max_length=10)),
                ('rented', models.BooleanField()),
                ('cost_per_night', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.room')),
                ('bathroom_size', models.CharField(max_length=2)),
                ('shower_type', models.CharField(choices=[('1', 'Shower'), ('2', 'Bath'), ('3', 'Combination Shower-Bath')], max_length=1)),
            ],
            bases=('booking.room',),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('standard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.standard')),
                ('kitchen_size', models.CharField(max_length=3)),
                ('kitchen_type', models.CharField(choices=[('1', 'Mini'), ('2', 'Full')], max_length=1)),
            ],
            bases=('booking.standard',),
        ),
    ]
