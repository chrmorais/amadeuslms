# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 18:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Subject', verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='subjectcategory',
            name='subjects',
            field=models.ManyToManyField(to='courses.Subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_category', to='courses.CategorySubject', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='courses.Course', verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(related_name='professors_subjects', to=settings.AUTH_USER_MODEL, verbose_name='Professors'),
        ),
        migrations.AddField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='subject_student', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='material',
            name='students',
            field=models.ManyToManyField(related_name='materials', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='material',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='linkmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_link', to='courses.Material', verbose_name='Material'),
        ),
        migrations.AddField(
            model_name='filematerial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_file', to='courses.Material', verbose_name='Material'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='courses.CourseCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(related_name='courses_professors', to=settings.AUTH_USER_MODEL, verbose_name='Professors'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_student', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='activityfile',
            name='diet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='courses.Activity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='students',
            field=models.ManyToManyField(related_name='activities', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='activity',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='courses.Topic', verbose_name='Topic'),
        ),
    ]
