# Generated by Django 2.2.2 on 2019-08-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_remove_employee_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='workstation',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
