# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 19:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_subject_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CourseCategory',
        ),
        migrations.AlterField(
            model_name='activity',
            name='limit_date',
            field=models.DateField(verbose_name='Deliver Date'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(related_name='professors_subjects', to=settings.AUTH_USER_MODEL, verbose_name='Professors'),
        ),
    ]
