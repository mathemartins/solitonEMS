# Generated by Django 2.2.3 on 2020-05-17 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('producer', models.CharField(max_length=40)),
                ('file_format', models.CharField(max_length=10)),
                ('year_published', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='resources')),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='organisation_details.Department')),
            ],
        ),
    ]
