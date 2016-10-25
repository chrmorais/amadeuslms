# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicFile',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Material')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('file_url', models.FileField(upload_to=files.models.file_path, verbose_name='File')),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_files', to='core.MimeType', verbose_name='Type file')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name_plural': 'Files',
                'verbose_name': 'File',
            },
            bases=('courses.material',),
        ),
    ]
