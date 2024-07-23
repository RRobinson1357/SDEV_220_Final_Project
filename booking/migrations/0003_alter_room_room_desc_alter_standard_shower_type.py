# Generated by Django 5.0.2 on 2024-07-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_room_room_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_desc',
            field=models.CharField(choices=[('Standard', 'desc'), ('Basic', 'desc'), ('Studio', 'desc')], max_length=10),
        ),
        migrations.AlterField(
            model_name='standard',
            name='shower_type',
            field=models.CharField(choices=[('1', 'Shower'), ('3', 'Combination Shower-Bath'), ('2', 'Bath')], max_length=1),
        ),
    ]