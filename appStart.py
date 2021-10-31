# import winapps
import os
# for app in winapps.list_installed():
#     print(app)
# print("111111")
# for app in winapps.search_installed(''):
#     print(app)
calculator = 'calc.exe'
notepad = 'notepad.exe'
calendar = 'iCloudWeb.exe'
list_notepad = ['notepad',"блокнот"]
list_calculator = ['calculator','калькулятор']
list_application = [calculator, notepad]
list_aplication1 = [list_calculator, list_notepad]

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def a1():
    for name_application in list_application:
        # if name_application in q:
        #     break
        a = find(name_application,'C:\Windows' )#'C:\Windows'
        file = open('store-apps-list.txt','a')
        file1 = open('store-apps-list.txt','r')
        q = file1.readlines()
        print(q)
        file1.close()
        # for line in q:
        #     print(line)
        #     print(name_application + " : " + str(a) + '\n')
        #     if line == name_application + " : " + str(a) + '\n':
        #         print(1)
        #         break
        # file.write(name_application + " : " + str(a) + '\n')
        file.close()
        # print(a)

def start_application(name):
    # print("qweqweqwe",name)
    for name_ in list_aplication1:
        if name in name_:
            # print(list_aplication1.index(name_))
            # print(11111)
            start_app(list_application[ list_aplication1.index(name_) ])
            break
    # print(1)
    # if name in list_name:
        # print(2)
def start_app(name):
    # print("name",name)
    file = open("store-apps-list.txt", 'r')
    q = file.readlines()
    for line in q:
        # print(line)
        # print(3)
        # tt = line.index(":")
        name_app_in_file = line[0:line.index(":") - 1]
        addres_app_in_file = line[line.index(":") + 2:-1]
        if name == name_app_in_file:
            os.startfile(addres_app_in_file)
        # print("name",name_app_in_file)
        # print("addres",addres_app_in_file)
    file.close()





# a1()
# start_application('калькулятор')
# import os
# print(os.name)
# a = os.listdir('C:\Windows\WinSxS')
# # file = open('test.txt','w')
# # file.write(str(a))
# # file.close()
# for b in a:
#     print(b)
#     c = b.split("")
#     file = open('test.txt', 'w')
#     file.write(str(b))
#     file.close()
# # print(a)
'asdwads'

# os.startfile('C:\Windows\WinSxS\wow64_microsoft-windows-calc_31bf3856ad364e35_10.0.18362.1_none_86701b88cc5528d8')