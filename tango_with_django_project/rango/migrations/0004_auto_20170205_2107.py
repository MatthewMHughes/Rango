# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_slugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slugs',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
