# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('cp', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('psc', models.IntegerField()),
            ],
        ),
    ]
