# Generated by Django 3.1.2 on 2020-10-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201023_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='Doctor_Appointment_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
