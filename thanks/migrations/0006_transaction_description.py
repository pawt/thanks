# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0005_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.TextField(default=''),
        ),
    ]