# Generated by Django 3.0.7 on 2020-08-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0004_auto_20200817_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeekpi',
            name='assessor',
            field=models.CharField(choices=[('HOD', 'Head of Department'), ('HR', 'Human Resource Officer'), ('Self', 'Self')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
