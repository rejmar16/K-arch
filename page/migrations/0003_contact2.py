# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('cp', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('psc', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]