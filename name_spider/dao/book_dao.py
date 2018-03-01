# -*- coding: utf-8 -*-
from mongoengine import *
from model.model import *
import time
import datetime

connect('hezz_writer', host='localhost', port=27017)

# 取系统时间
def get_system_time ():
    return int(time.time() *1000)

def save_book(**args):
    # book = Book('史记', '山寨史记', 200, '贺政忠', get_system_time())
    book = Book(args['title'],args['summary'],args['chapter_num'],args['author'],args['ctime'])
    book.save()

ctime = get_system_time();
# save_book(title = '史记', summary='山寨史记', chapter_num=200, author='贺政忠', ctime=get_system_time())

# books = Book.objects.all()
#
# for b in books:
#     print b.id

book = Book.objects.get(id = '5a97bb7bb1166133f813f1f7')
book.title = '春秋新传2'
book.save()

