# Generated by Django 3.0.5 on 2020-04-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0005_auto_20200427_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='check_in',
            field=models.CharField(choices=[('Entire place', 'Entire place'), ('Private room', 'Private room'), ('Shared room', 'Shared room')], default='Lockbox', max_length=30),
        ),
        migrations.AlterField(
            model_name='stay',
            name='home_types',
            field=models.CharField(choices=[('Entire place', 'Entire place'), ('Private room', 'Private room'), ('Shared room', 'Shared room')], default='Entire place', max_length=30),
        ),
    ]
