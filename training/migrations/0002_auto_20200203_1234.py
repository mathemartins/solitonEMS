# Generated by Django 3.0 on 2020-02-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='employee',
            new_name='applicant',
        ),
        migrations.AddField(
            model_name='training',
            name='HOD_approval',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='training',
            name='HR_approval',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='training',
            name='ceo_approval',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='training',
            name='cfo_approval',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='training',
            name='supervisor_approval',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
