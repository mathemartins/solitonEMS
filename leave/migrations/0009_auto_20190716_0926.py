# Generated by Django 2.2.1 on 2019-07-16 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0008_leaveapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='apply_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]