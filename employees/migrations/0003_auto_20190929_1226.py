# Generated by Django 2.2.2 on 2019-09-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190929_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='basic_salary',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lunch_allowance',
            field=models.IntegerField(default=150000),
        ),
    ]
