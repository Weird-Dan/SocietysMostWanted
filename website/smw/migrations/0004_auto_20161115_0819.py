# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smw', '0003_auto_20161111_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Background_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='Icon_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
