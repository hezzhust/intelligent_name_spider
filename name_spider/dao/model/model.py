# -*- coding: utf-8 -*-
from mongoengine import *
# 书籍 用于存放 书籍概要信息
class Book(Document):
    title = StringField(required=True, max_length=200)
    summary = StringField();#简介
    chapter_num = IntField() # 章节数
    author = StringField() # 作者
    ctime = LongField(required=True)
    mtime = LongField()


#章节
class Chapter(Document):
    title = StringField()
    book_id = StringField()
    content = StringField()
    ctime = LongField()
    mtime = LongField()
    order_num = IntField()#章节号