# Generated by Django 3.0.5 on 2020-04-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('stays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='reviews.Review'),
        ),
    ]
