# Generated by Django 4.1.3 on 2023-05-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_From_ASV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humdinity', models.DecimalField(decimal_places=6, max_digits=9)),
                ('temperature', models.DecimalField(decimal_places=6, max_digits=9)),
                ('dissolvedOxygen', models.DecimalField(decimal_places=6, max_digits=9)),
                ('airPressure', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Data_From_Gps_To_Web',
        ),
        migrations.DeleteModel(
            name='Data_From_Sensor',
        ),
        migrations.DeleteModel(
            name='SensorData',
        ),
        migrations.AddField(
            model_name='response_from_web',
            name='zone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
