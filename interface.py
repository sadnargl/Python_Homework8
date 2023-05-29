from os import system
from functions import *
choise = ""
filename = "directory.txt"
while choise != "6":
    system('cls')
    print ("1. Добавить контакт")
    print ("2. Вывести все контакты")
    print ("3. Поиск по фамилии")
    print ("4. Изменить контакт")
    print ("5. Удалить контакт")
    print ("6. Выход из программы")
    print ("-------------------")
    choise = input ("Выберите номер меню: ",)
    print ()
    match choise:
        case "1": 
            add (filename,input ("Введите контакт, ФИО и Телефон, разделитель пробелл: "))
        case "2":
            printall (filename)
        case "3":
            search (filename, input ("Введите строку для поиска контакта, с учетом регистра: "))
        case "4":
            change (filename, input ("Введите строку для изменения контакта. Можно ввести часть строки: "), input ("Введите на что необходимо заменить. Строка должна быть введена полностью, ФИО и телефон: ")) 
        case "5":
            remove (filename, input ("Введите строку для удаления контакта, с учетом регистра. Можно ввести часть строки: "))            
        case "6":
            print ("До свидания")
        case _:
            print ("Неправильный ввод. Повторите")