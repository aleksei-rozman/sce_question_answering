from bs4 import BeautifulSoup
import requests
# import os
import search_in_wiki
import json


def start_searh(text_search):
    global title, list_addr
    url, title, list_addr = search_in_wiki.search_wiki(text_search=text_search) # поиск в вике
    # print("\n\nurl",url)
    # print("\n\ntitle",title)
    # print("\n\ntitle",list_addr)
    # print("\n\nurl",)
    # print("aaaaaaaaaa",url)
    return url  # "https://en.wikipedia.org/wiki/Web_scraping"


def get_html(url):
    return requests.get(url).text # возвращает страницу в html формате


def parseee(text_search): #парсинг страници с статьей
    # print("\n\n\n333333333333333333333333333333333333333333333333333333333333\n\n\n")
    output = ""
    # print("aaaaa",text_search)
    url = start_searh(text_search)
    # print("\n\n\nurl",url,"\n\n\n\n\n")
   
    html = get_html(url)
    # print("\n\n\n\nhtml",html,"\n\n\n\n")
    soup = BeautifulSoup(html, features="lxml")
    # print("\n\nsoup",soup,"\n\n\n\n")
    # print("\n\n\n222222222222222222222222222222222222222222222222222222222222\n\n\n")
    labels = soup.select("div#toc li a")
    # print("\n\nlabels",labels)
    if labels == None:
        # print("\n\n\n111111111111111111111111111111111111111111111111111111111\n\n\n")
        html = get_html(list_addr[1])
        soup = BeautifulSoup(html, features="lxml")
    
        labels = soup.select("div#toc li a")
    for i in labels:
        output = output + i.getText()+'\n'
    output =url + '\n' + output
    return title, output, list_addr

    

    


