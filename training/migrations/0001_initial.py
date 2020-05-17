# Generated by Django 2.2.3 on 2020-05-17 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(max_length=30)),
                ('duration', models.IntegerField()),
                ('venue', models.CharField(max_length=40)),
                ('purpose', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(max_length=40)),
                ('institution', models.CharField(max_length=40)),
                ('duration', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('business_case', models.TextField(blank=True)),
                ('objectives', models.TextField(blank=True)),
                ('preparations', models.TextField(blank=True)),
                ('skills', models.CharField(blank=True, max_length=40)),
                ('knowledge', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('supervisor_approval', models.CharField(default='Pending', max_length=10)),
                ('HOD_approval', models.CharField(default='Pending', max_length=10)),
                ('HR_approval', models.CharField(default='Pending', max_length=10)),
                ('cfo_approval', models.CharField(default='Pending', max_length=10)),
                ('ceo_approval', models.CharField(default='Pending', max_length=10)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('currency', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Currency')),
            ],
        ),
    ]
