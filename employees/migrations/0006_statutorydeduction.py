# Generated by Django 3.0.7 on 2020-09-28 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_local_service_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatutoryDeduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_service_tax', models.IntegerField(default=0)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
    ]
