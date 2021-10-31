key = '<use_your_key>'
import telebot
import start
import audioTooText
import pars_table
from rutermextract import TermExtractor

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(
    key, threaded=True)
global str_a
# global message
# global
list_addr = ""
title = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    send_mesages(message, 1)
    tr = message.from_user
    tr = str(tr)
    tr = tr.split(",")
    for tr1 in tr:

        print(tr1)


@bot.message_handler(content_types=['voice'])
def listener(message):
    
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    message_text = str(audioTooText.startDecod())
    send_mesages(message, message_text)

# def pars_table.s_tabl_a(title,message_text):
#     # title = "Python_(programming language)"
#     import pars_table
#     out = ""
#     if title == "":
#         return "ERROR :use search first \n try find"
#     else:
#         # print(message_text)
#         message_text = message_text.split(" ")
#         # print(message_text)
#         index = message_text.index("/table")
#         # print(index)
#         del message_text[index]
#         message_text= str(message_text)

#         message_text = int(message_text[2:-2])
#         out = pars_table.parse_paje_whith_table(name=title , int_in_table=message_text)

#     return out
# n = 0
def num_exept(n):
    n = n +1
    return n 
number = 0
# global 

def try_send(message,message_text):
    
    global title, str_a, list_addr,number
    str_a = ''
    number = number + 1

    # print(message_text)
    title, str_a, list_addr = start.start_find(message_text)
    str_a = str_a.split("\n")
    # print(list_addr)

    print(title)
    # bot.send_message(message.from_user.id, str(title))
    m = 0
    for out in str_a:
        if out != '':
            if m != 0:
                out = out.split(" ")
                list_out = out[1:]
                out = ""
                for a in list_out:
                    out = out + str(a)+ " "
            # print(m)
            if m == 0:
                bot.send_message(message.from_user.id, str(out))
            else:
                bot.send_message(message.from_user.id, str(m)+") "+str(out))
            m+=1

def send_mesages(message, a):
    global list_addr, title 
    
    # print()
 
    if a == 1:
        message_text = message.text
    else:
        message_text = a

    if "find" in message_text:
 
        number = 0
        
        try:

            try_send(message,message_text)
            
        except:
            if number <5:
                print("\n\ntry send",number,"\n\n\n")
                try:
                    try_send(message,message_text)
                except:
                    bot.send_message(
                        message.from_user.id, "I honestly tried but something went wrong \ntry to change the search keyword ")

            # else:
            # print("\n\n\nEXETP!!!!!!!!!!!!\n\n\n")
            # number = num_exept(number)
            # start.remember(number)
            # title, str_a, list_addr = start.start_find(message_text)
                # bot.send_message(
                #     message.from_user.id, "I honestly tried but something went wrong \ntry to change the search keyword ")

    elif message_text == "/help":
        try:
            bot.send_message(message.from_user.id, "I will find information in wikipedia\nStart your search with the keyword 'find'\nAfter searching, see the data in the table:'/select numfer_in_table'\n List of all found articles /back")
        except :
            print("error")
        
    elif message_text == "/back":
        try:
            if list_addr != None:
                bot.send_message(message.from_user.id, str(title))
                num = 1
                for line in list_addr:
                    
                    bot.send_message(message.from_user.id, str( str(num)+ ") " + line))
                    num= num +1
    
            else:
                bot.send_message(message.from_user.id, "Not Page")
        except:
            bot.send_message(message.from_user.id, "Not Page")
    elif "/select" in message_text:
        term_extractor = TermExtractor()
        try:
            # print(message_text)
            out = pars_table.s_tabl_a(title,message_text)
            out = out.split("\n")

            for l in out:
                if l != '':
                    bot.send_message(message.from_user.id, str(l))
          
            keywords = "keywords : \n"            
            for term in term_extractor(str(out))[:10]:
                keywords = keywords + "* "+str(str(term.normalized)+" "+ str(term.count)) +" *"+ "\n"
            bot.send_message(message.from_user.id,keywords)
            # print("a")
    # elif message_text == "aaa":
    #     message_handler(message)
        except:
            bot.send_message(message.from_user.id, "Error in syntax table\ntry '/find (table numbers)")
    else:
        bot.send_message(message.from_user.id,
                         "I don’t understand you. Write /help.")


def gen_markup():
    markup=InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # print(call)
    if call.data == "cb_yes":
        # for line in list_addr:
            # bot.send_message(call.from_user.id, str(line))
        bot.answer_callback_query(call.id, "Answer is Yes aaaaaa")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@ bot.message_handler(func=lambda message: True)
def message_handler(message):
    # print(message)
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())


# print(str_a)
# bot.set_update_listener(listener)
bot.polling(none_stop=True, interval=0)



