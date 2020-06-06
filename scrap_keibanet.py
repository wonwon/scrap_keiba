#import requests
#from bs4 import beautifulsoup
#import re
#import time
from class_sqlite import Database

with Database('db_netkeiba.sqlite') as db:
    db.execute('CREATE TABLE race(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        race_id INTEGER,\
        date varchar(50),\
        weather integer,\
        groundcon integer,\
        quantity integer,\
        rank integer,\
        sex integer,\
        age integer,\
        results integer,\
        favorite integer,\
        ration integer,\
        racetype varchar(100),\
        location varchar(100),\
        jockey INTEGER,\
        horseid INTEGER,\
        refund integer)\
        ')
    #db.execute('CREATE TABLE stock_info(id INTEGER PRIMARY KEY AUTOINCREMENT, code INTEGER, date varchar(20), open integer, close integer, hight integer, low integer, volume integer)')
    #db.execute('CREATE TABLE credit_info(id INTEGER PRIMARY KEY AUTOINCREMENT, code INTEGER, date varchar(50), marginbuy integer, marginsale iteger, ratio integer)')
