# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topics', '0007_auto_20170123_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webconference',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='topics.Resource')),
                ('presentation', models.TextField(blank=True, verbose_name='Presentation')),
                ('start', models.DateTimeField(verbose_name='Start date/hour')),
                ('end', models.DateTimeField(verbose_name='End date/hour')),
            ],
            options={
                'verbose_name_plural': 'Web Conferences',
                'verbose_name': 'Web Conference',
            },
            bases=('topics.resource',),
        ),
    ]
