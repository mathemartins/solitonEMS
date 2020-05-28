# Generated by Django 3.0 on 2020-05-28 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OvertimePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('HR_approval', models.CharField(default='Pending', max_length=10)),
                ('cfo_approval', models.CharField(default='Pending', max_length=10)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('applicant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='OvertimeSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number_of_hours', models.IntegerField(blank=True)),
                ('description', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('overtime_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='overtime.OvertimePlan')),
            ],
        ),
        migrations.CreateModel(
            name='OvertimeApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('date', models.DateField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('supervisor_approval', models.CharField(default='Pending', max_length=10)),
                ('HOD_approval', models.CharField(default='Pending', max_length=10)),
                ('HR_approval', models.CharField(default='Pending', max_length=10)),
                ('cfo_approval', models.CharField(default='Pending', max_length=10)),
                ('ceo_approval', models.CharField(default='Pending', max_length=10)),
                ('applicant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='employees.Employee')),
            ],
        ),
    ]
