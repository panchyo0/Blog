# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180422_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Content',
            field=models.TextField(),
        ),
    ]