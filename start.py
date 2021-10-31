
import parserrr

del_text_find = ["find", "найди"] #ключевое слово

def start_find(text):
    # print("aaaaaaa",text)
    text_seach = ''
    text = text.lower()
    text1 = text.split(" ")
    find = ""
    for dell in del_text_find:
        if dell in text1:
            index = text1.index(dell)
            del text1[index]
 
            for a in text1:
                text_seach = text_seach+" "+ a
            title, find, list_addr = parserrr.parseee(str(text_seach[1:]))# парсинг страници вики
            break

    return title, find , list_addr
global n 
n = 0
def send_n():
    return n

def remember(n):
    n = n
 

# def 

