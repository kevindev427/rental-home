# Generated by Django 3.0.5 on 2020-04-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]