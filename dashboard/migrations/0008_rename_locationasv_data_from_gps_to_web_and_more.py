# Generated by Django 4.1.3 on 2023-05-16 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_datamonitoring'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='locationASV',
            new_name='Data_From_Gps_To_Web',
        ),
        migrations.RenameModel(
            old_name='dataMonitoring',
            new_name='Data_From_Sensor',
        ),
        migrations.RenameModel(
            old_name='GPSGetPoint',
            new_name='Response_From_Web',
        ),
    ]
