# Generated by Django 4.1.3 on 2023-06-07 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_rename_date_data_from_asv_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_from_asv',
            old_name='humdinity',
            new_name='humidity',
        ),
    ]