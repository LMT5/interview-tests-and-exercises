import sys
import requests
import json
from bs4 import BeautifulSoup
zh2CN = {}
zh2Hans = {}
zh2Hant = {}
zh2HK = {}
zh2TW = {}
def create_table():
    global zh2CN,zh2Hans,zh2Hant,zh2HK,zh2TW
    #read zh2CN data
    f = open('zh2CN.txt','r')
    s = f.read()
    s = s.replace("\'", "\"")
    s = s.replace('\n','')
    s = s.replace('=>',':')
    s = s.replace(' ','')
    s = s.replace('\r','')
    zh2CN = json.loads(s)
    f.close()
    #read zh2Han data
    f = open('zh2Hans.txt','r')
    s = f.read()
    s = s.replace("\'", "\"")
    s = s.replace('\n','')
    s = s.replace('=>',':')
    s = s.replace(' ','')
    s = s.replace('\r','')
    zh2Hans = json.loads(s)
    f.close()
    #read zh2Hant data
    f = open('zh2Hant.txt','r')
    s = f.read()
    s = s.replace("\'", "\"")
    s = s.replace('\n','')
    s = s.replace('=>',':')
    s = s.replace(' ','')
    s = s.replace('\r','')
    zh2Hant = json.loads(s)
    f.close()
    #read zh2HK data
    f = open('zh2HK.txt','r')
    s = f.read()
    s = s.replace("\'", "\"")
    s = s.replace('\n','')
    s = s.replace('=>',':')
    s = s.replace(' ','')
    s = s.replace('\r','')
    zh2HK = json.loads(s)
    f.close()
    # read zh2TW data
    f = open('zh2TW.txt','r')
    s = f.read()
    s = s.replace("\'", "\"")
    s = s.replace('\n','')
    s = s.replace('=>',':')
    s = s.replace(' ','')
    s = s.replace('\r','')
    zh2TW = json.loads(s)
    f.close()

def crawler(search,page):
    count = 0
    #relevancy sales ctime
    #page = 1 
    #https://shopee.tw/api/v4/search/search_items?by=relevancy&fe_categoryids=11041645&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2
    response = requests.get("https://shopee.tw/api/v4/search/search_items?by="+ str(search) +"&fe_categoryids=11041645&limit=60&newest=" + str(60 * (int(page) - 1)) + "&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2")
    response.encoding = 'uft-8'
    search = response.text
    goods = json.loads(search)
    for i in range(len(goods['items'])):
        count+=1
        print("繁體 : ",goods['items'][i]['item_basic']['name'])
        print("簡體 : ",transform(goods['items'][i]['item_basic']['name']))
        if(goods['items'][i]['item_basic']['price_min'] == goods['items'][i]['item_basic']['price_max']):
            print("$",goods['items'][i]['item_basic']['price']/100000)
        else:
            print("$",goods['items'][i]['item_basic']['price_min']/100000,"- $",goods['items'][i]['item_basic']['price_max']/100000)
    

def transform(name):
    text = name
    #zh2CN 繁:簡
    keys = list(zh2CN.keys())
    for i in range(len(zh2CN)):
        txt1 = zh2CN[keys[i]].replace("'","")
        txt2 = keys[i].replace("'","")
        if(txt2 in name):
            text = text.replace(txt2,txt1)

    #zh2Hans 繁:簡
    keys = list(zh2Hans.keys())
    for i in range(len(zh2Hans)):
        txt1 = zh2Hans[keys[i]].replace("'","")
        txt2 = keys[i].replace("'","")
        if(txt2 in name):
            text = text.replace(txt2,txt1)

    #zh2Hant 簡:繁
    keys = list(zh2Hans.keys())
    for i in range(len(zh2Hans)):
        txt1 = zh2Hans[keys[i]].replace("'","")
        txt2 = keys[i].replace("'","")
        if(txt1 in name):
            text = text.replace(txt1,txt2)

    #zh2HK 簡:繁
    keys = list(zh2HK.keys())
    for i in range(len(zh2HK)):
        txt1 = zh2HK[keys[i]].replace("'","")
        txt2 = keys[i].replace("'","")
        if(txt1 in name):
            text = text.replace(txt1,txt2)

    #zh2TW 簡:繁
    keys = list(zh2TW.keys())
    for i in range(len(zh2TW)):
        txt1 = zh2TW[keys[i]].replace("'","")
        txt2 = keys[i].replace("'","")
        if(txt1 in name):
            text = text.replace(txt1,txt2)

    return text

create_table()
crawler(sys.argv[1],sys.argv[2])
