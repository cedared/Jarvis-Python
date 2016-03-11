# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('message_id', models.TextField(max_length=20)),
                ('title', models.TextField(max_length=255)),
                ('content', models.TextField()),
                ('authorId', models.TextField(max_length=20)),
                ('isLocked', models.BooleanField()),
                ('isAnonymity', models.BooleanField()),
                ('created', models.TimeField()),
                ('updated', models.TimeField()),
                ('isDeleted', models.BooleanField()),
                ('commentsCount', models.IntegerField()),
                ('likeCount', models.IntegerField()),
                ('isTopped', models.BooleanField()),
                ('isDouban', models.BooleanField()),
                ('dbtid', models.IntegerField()),
                ('isElited', models.BooleanField()),
                ('isLiked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PhotoItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('photo_id', models.TextField(max_length=20)),
                ('seqId', models.IntegerField()),
                ('url', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('userId', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('avatar', models.URLField()),
                ('user_id', models.TextField(max_length=20)),
            ],
        ),
    ]
