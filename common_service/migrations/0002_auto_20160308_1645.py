# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageitem',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photoitem',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
