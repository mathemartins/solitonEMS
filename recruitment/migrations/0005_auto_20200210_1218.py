# Generated by Django 3.0 on 2020-02-10 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation_details', '0001_initial'),
        ('recruitment', '0004_auto_20200130_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobadvertisement',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='organisation_details.Position'),
        ),
    ]
