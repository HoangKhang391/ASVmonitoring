# Generated by Django 4.1.3 on 2023-05-28 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_location_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]