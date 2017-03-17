# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 10:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0004_auto_20170315_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_given', models.IntegerField(default=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giver', to='thanks.Employee')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='thanks.Employee')),
            ],
        ),
    ]
