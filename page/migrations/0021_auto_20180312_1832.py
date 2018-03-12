# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-12 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0020_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screen',
            field=models.ImageField(default='screen_folder/None/no-img.jpg', upload_to='static/screen_folder/'),
        ),
        migrations.AlterField(
            model_name='project_photo',
            name='photo',
            field=models.ImageField(default='photo_folder/None/no-img.jpg', upload_to='static/photo_folder/'),
        ),
        migrations.AlterField(
            model_name='vizualizace',
            name='screen',
            field=models.ImageField(default='screen_folder/None/no-img.jpg', upload_to='static/screen_folder/'),
        ),
    ]