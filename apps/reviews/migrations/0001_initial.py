# Generated by Django 3.0.5 on 2020-05-02 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=1250)),
                ('rating', models.IntegerField(blank=True, default=5, null=True)),
                ('location', models.IntegerField(blank=True, default=5, null=True)),
                ('cleanliness', models.IntegerField(blank=True, default=5, null=True)),
                ('hospitality', models.IntegerField(blank=True, default=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]