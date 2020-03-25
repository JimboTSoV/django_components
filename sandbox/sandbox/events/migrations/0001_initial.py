# Generated by Django 3.0.2 on 2020-03-20 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=600, verbose_name='Description')),
                ('picture', models.CharField(blank=True, max_length=200, verbose_name='Picture')),
            ],
        ),
    ]