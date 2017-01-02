# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-02 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20161226_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='coordinators',
            field=models.ManyToManyField(null=True, related_name='coordinators', to=settings.AUTH_USER_MODEL),
        ),
    ]