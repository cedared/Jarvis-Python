from django.test import TestCase

import json
import os
# Create your tests here.


class FileReader(object):
    def __init__(self):
        self.file_path = '/Users/albert/Desktop/haixiu1.txt'

    def get_data(self):
        from models import MessageItem, PhotoItem, UserItem
        with open(self.file_path, 'rb') as f:
            for each in f.readlines():
                line = json.loads(each)
                # message = MessageItem()
                # photo = PhotoItem()
                # user = UserItem()
                print line["topics"][0]


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Jarvis.settings")
    test = FileReader()
    test.get_data()