# Generated by Django 3.0.2 on 2020-03-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventteaser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.FileField(blank=True, max_length=200, upload_to='', verbose_name='Picture'),
        ),
    ]
