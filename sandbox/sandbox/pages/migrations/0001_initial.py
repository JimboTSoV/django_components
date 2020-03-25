# Generated by Django 3.0.2 on 2020-03-20 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('url_path', models.CharField(blank=True, max_length=200, verbose_name='Url Path')),
            ],
        ),
        migrations.CreateModel(
            name='PageType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('base_template_path', models.CharField(max_length=400, verbose_name='Base Template Path')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceholderType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('page_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placeholders', to='pages.PageType', verbose_name='Page Type')),
            ],
        ),
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeholders', to='pages.Page', verbose_name='Page')),
                ('placeholder_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeholders', to='pages.PlaceholderType', verbose_name='Placeholder Type')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.PageType', verbose_name='Page Type'),
        ),
        migrations.CreateModel(
            name='ComponentType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('template_name', models.CharField(max_length=400, null=True, verbose_name='Template Name')),
                ('registered_placeholders', models.ManyToManyField(related_name='component_types', to='pages.PlaceholderType', verbose_name='Registered Placeholders')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('object_id', models.UUIDField(default=uuid.uuid4, editable=False, null=True)),
                ('component_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ComponentType', verbose_name='Component Type')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('placeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='pages.Placeholder', verbose_name='Placeholder')),
            ],
        ),
        migrations.AddConstraint(
            model_name='placeholder',
            constraint=models.UniqueConstraint(fields=('page', 'placeholder_type'), name='unique_placeholder'),
        ),
        migrations.AddConstraint(
            model_name='page',
            constraint=models.UniqueConstraint(fields=('url_path', 'slug'), name='unique_url'),
        ),
    ]