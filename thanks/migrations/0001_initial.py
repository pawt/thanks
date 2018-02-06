# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-06 19:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_to_give', models.IntegerField(default=100)),
                ('points_collected', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('points_given', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giver', to='thanks.Employee')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='thanks.Employee')),
            ],
        ),
    ]
