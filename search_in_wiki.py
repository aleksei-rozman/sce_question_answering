
import wikipedia
# import start_telegram_bot
import start
def search_wiki(text_search):
    sear = ""
    ny = ""
    print(text_search)

    if len(text_search) != 0:
        try:
            # n =start.send_n()
            # print("nnnnnnnnnnnnnnnnnn",n)
            # print("asdwasdw",text_search)
            ny = wikipedia.page(text_search) 
            # print("\n\n\nny",ny,"\n\n\n")
            sear = wikipedia.search(text_search)# получение списка ссылок после поиска
            # print("asdwasdwaasd",sear)
            # print(ny)
            
        except :
            ny = wikipedia.page("a")
            ny.url = "https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&go=Go"
            ny.title = "Page Not Find try again"
            for l1 in sear:
                try:
                    n1 = wikipedia.page(l1)
                    cheak_libr = cheak_libr + ',' + str(n1.url)
                except:
                    cheak_libr = cheak_libr
            cheak_libr = cheak_libr[1:].split(",")
            return ny.url, ny.title, cheak_libr
    else:
        ny = wikipedia.page("a")
        ny.url = "https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&go=Go"
        ny.title = "Page Not Find try again"
        cheak_libr = None
        return ny.url, ny.title, cheak_libr
    cheak_libr = ""
    # print("\n\n\nsear",sear,"\n\n\n\n")
    for l1 in sear:
        
        try:
            n1 = wikipedia.page(l1)
            cheak_libr = cheak_libr + ',' + str(n1.url)
        except:
            cheak_libr = cheak_libr
    cheak_libr = cheak_libr[1:].split(",")
    # print("aaaaaa",cheak_libr)
    return ny.url, ny.title, cheak_libr
"""
ny.url - найденная статья
ny.title - название статьи
cheak_libr - список всех найденных статей
"""


# search_wiki("memas")