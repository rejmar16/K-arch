# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_vizualizace_vizualizace_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vizualizace_photo',
            name='vizualizace',
        ),
        migrations.RemoveField(
            model_name='vizualizace',
            name='text',
        ),
        migrations.AlterField(
            model_name='vizualizace',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Vizualizace_Photo',
        ),
    ]
