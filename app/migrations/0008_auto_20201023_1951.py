# Generated by Django 3.1.2 on 2020-10-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201023_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='Doctor_Appointment_Date',
            field=models.DateTimeField(default=None),
        ),
    ]
