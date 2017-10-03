# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0058_auto_20170822_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='report_format',
            field=models.CharField(choices=[(b'base64', b'base64'), (b'base64bz2', b'base64bz2')], default=b'base64bz2', editable=False, max_length=256),
        ),
    ]
