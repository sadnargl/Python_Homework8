import os
def printall (filename):
    with open (filename,"r", encoding="ANSI") as data:
        for line in data:
            print (line, end="")
    input ("\nНажмите Enter для возврата в меню",)

def search (filename, arg, encoding="ANSI"):
    with open (filename,"r") as data:
       for line in data:
            if arg in line:
                print (line, end="")
    input ("\nНажмите Enter для возврата в меню",)

def add (filename, arg, encoding="ANSI"):
    with open (filename,"a") as data:
        data.writelines (f"{arg}\n")
    input ("\nНажмите Enter для возврата в меню",)

def remove (filename, arg, encoding="ANSI"):
    counter = 0
    with open (filename,"r+") as data:
        with open ("temp.txt","w") as temp:
            for line in data:
                if arg in line:
                    temp.writelines ('')
                    counter += 1
                else:
                    temp.writelines (line)
    os.remove (filename)
    os.rename ("temp.txt", filename)
    if counter == 0:
        print ("Контакты не найдены")
    else:
           print (f"Удалено {counter} контакта")
    input ("\nНажмите Enter для возврата в меню",)

def change (filename, arg, arg_replace, encoding="ANSI"):
    counter = 0
    with open (filename,"r+") as data:
        with open ("temp.txt","w") as temp:
            for line in data:
                if arg in line:
                    temp.writelines (f"{arg_replace}\n")
                    counter += 1
                else:
                    temp.writelines (line)
    os.remove (filename)
    os.rename ("temp.txt", filename)
    if counter == 0:
        print ("Контакты не найдены")
    else:
           print (f"Изменено {counter} контакта") 
    input ("\nНажмите Enter для возврата в меню",)