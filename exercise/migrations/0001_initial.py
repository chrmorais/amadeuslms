# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20161117_0009'),
        ('core', '0002_auto_20161117_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('init_date', models.DateField(verbose_name='Begin of Subject Date')),
                ('end_date', models.DateField(verbose_name='End of Subject Date')),
                ('grade', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('professors', models.ManyToManyField(blank=True, related_name='professors_exercise', to=settings.AUTH_USER_MODEL, verbose_name='Professors')),
                ('students', models.ManyToManyField(blank=True, related_name='subject_exercise', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='courses.Topic', verbose_name='Topic')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='exercise.Exercise')),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_files', to='core.MimeType', verbose_name='Type file')),
            ],
        ),
    ]
