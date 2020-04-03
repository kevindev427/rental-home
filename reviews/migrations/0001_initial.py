# Generated by Django 3.0.5 on 2020-04-02 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stays', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=1250)),
                ('stars', models.IntegerField(default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Stays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stays.Stays')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]