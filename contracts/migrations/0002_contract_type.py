# Generated by Django 3.0.7 on 2020-07-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='type',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]