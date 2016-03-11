from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MessageItem(models.Model):
    message_id = models.TextField(max_length=20)
    title = models.TextField(max_length=255)
    content = models.TextField()
    authorId = models.TextField(max_length=20)
    isLocked = models.BooleanField()
    isAnonymity = models.BooleanField()
    created = models.TextField()
    updated = models.TextField()
    isDeleted = models.BooleanField()
    commentsCount = models.IntegerField()
    likeCount = models.IntegerField()
    isTopped = models.BooleanField()
    isDouban = models.BooleanField()
    dbtid = models.IntegerField()
    isElited = models.BooleanField()
    isLiked = models.BooleanField()


class PhotoItem(models.Model):
    photo_id = models.TextField(max_length=20)
    seqId = models.IntegerField()
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    userId = models.TextField(max_length=20)


class UserItem(models.Model):
    name = models.TextField()
    avatar = models.URLField()
    user_id = models.TextField(max_length=20)