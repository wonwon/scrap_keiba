import requests
from bs4 import BeautifulSoup
import re
import time
from DB import class_sqlite

base_uri ='https://db.netkeiba.com/'
list_uri = 'race/list/20200229/'

def uri2soup(uri):
    html = requests.get(uri)
    html.encoding = 'EUC-JP'
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def ext_racelist(soup):
    lists = soup.select('a[href*="/race/202009"]')
    return lists

uri = base_uri + list_uri
soup = uri2soup(uri)
race_list = ext_racelist(soup)
for race in race_list:
    print(race.text)
    print(race['href'])


    #db.execute('CREATE TABLE stock_info(id INTEGER PRIMARY KEY AUTOINCREMENT, code INTEGER, date varchar(20), open integer, close integer, hight integer, low integer, volume integer)')
    #db.execute('CREATE TABLE credit_info(id INTEGER PRIMARY KEY AUTOINCREMENT, code INTEGER, date varchar(50), marginbuy integer, marginsale iteger, ratio integer)')
