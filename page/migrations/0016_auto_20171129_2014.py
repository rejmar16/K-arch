# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
