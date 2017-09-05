# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 15:03
from __future__ import unicode_literals

import bulletin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_auto_20170719_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='indicators',
            field=models.FileField(blank=True, null=True, upload_to='bulletin/indicators', validators=[bulletin.models.validate_file_extension], verbose_name='Relevant Indicators'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='file_content',
            field=models.FileField(blank=True, upload_to='bulletin/goals', validators=[bulletin.models.validate_file_extension], verbose_name='Goals'),
        ),
    ]