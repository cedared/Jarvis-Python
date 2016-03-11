from django.shortcuts import render
from models import MessageItem, PhotoItem, UserItem
from django.http import HttpResponse
import json
# Create your views here.


def get_data(request):
    with open('/Users/albert/Desktop/haixiu1.txt', 'rb') as f:
        line_number = 1
        for each in f.readlines():
            line = json.loads(each)
            datas = line["topics"]
            for each_data in datas:
                print line_number
                message = MessageItem()
                message.message_id = each_data['id']
                message.title = each_data['title']
                message.content = each_data['content']
                message.authorId = each_data['authorId']
                message.isLocked = each_data['isLocked']
                message.isAnonymity = each_data['isAnonymity']
                message.created = each_data['created']
                message.updated = each_data['updated']
                message.isDeleted = each_data['isDeleted']
                message.commentsCount = each_data['comments_count']
                message.likeCount = each_data['like_count']
                message.isTopped = each_data['isTopped']
                message.isDouban = each_data['isDouban']
                try:
                    message.dbtid = each_data['dbtid']
                except KeyError as e:
                    message.dbtid = 0
                message.isElited = each_data['isElited']
                message.isLiked = each_data['isLiked']
                message.save()
                user = UserItem()
                user.user_id = each_data['author']['id']
                user.avatar = each_data['author']['avatar']
                user.name = each_data['author']['name']
                user.save()
                try:
                    photos = each_data['photos']
                    for each_photo in photos:
                        photo = PhotoItem()
                        photo.photo_id = each_photo['id']
                        photo.seqId = each_photo['seqId']
                        photo.url = each_photo['url']
                        photo.width = each_photo['size']['width']
                        photo.height = each_photo['size']['height']
                        photo.userId = user.id
                        photo.save()
                except KeyError as e:
                    pass


                line_number += 1


    return HttpResponse("Hello World")




