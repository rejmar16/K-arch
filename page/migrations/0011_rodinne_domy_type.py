# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_rodinne_domy_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rodinne_domy',
            name='type',
            field=models.CharField(blank=True, choices=[('RD', 'Rodinne domy'), ('INTER', 'Interiery'), ('JINE', 'Jine')], max_length=10, null=True),
        ),
    ]