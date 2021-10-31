import json
from bs4 import BeautifulSoup
import subprocess
import os
from subprocess import Popen, PIPE, STDOUT


def parse_paje_whith_table(name,int_in_table): #скачивание файла
    out = ""
    int_in_table = str(int(int_in_table)+1)
    addr1 = "https://en.wikipedia.org/w/api.php?action=parse&section="+int_in_table+"&prop=text&page="+name+"&format=json"
    addr2 = "api.php?action=parse&section="+int_in_table+"&prop=text&page="+name+"&format=json"
    print(addr1)
    print(addr2)
    wget = Popen(['/usr/bin/wget', addr1], stdout=PIPE, stderr=STDOUT)
    stdout, nothing = wget.communicate()
    src = addr2
    dst = "text.json"
    os.rename(src,dst,src_dir_fd=None, dst_dir_fd=None) 
    



    with open("text.json", "r") as file: # парсинг json файла
        json_data = json.load(file)
    a = json_data["parse"]["text"]["*"]
    soup = BeautifulSoup(a, features="lxml")

    labels = soup.find_all('p')
    for i in labels:
         out = out+i.getText()+ '\n'
    return out

def s_tabl_a(title,message_text):# парсинг статьи по таблице
    out = ""
    if title == "":
        return "ERROR :use search first \n try find"
    else:
        message_text = message_text.split(" ")
        index = message_text.index("/select")
        del message_text[index]
        message_text= str(message_text)

        message_text = int(message_text[2:-2])
        out = parse_paje_whith_table(name=title , int_in_table=message_text-1)

    return out
