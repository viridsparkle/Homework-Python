# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from os.path import exists
from create import create 
from write import write_in_file
from search import search
from delete import delete
from change import change
from rewrite import rewrite

def menu():
    print('\n               Меню                  \n' +
          'Нажмите 1, чтобы просмотреть все записи\n' + 
          'Нажмите 2, чтобы внести новую запись\n' +
          'Нажмите 3, чтобы найти запись\n' +
          'Нажмите 4, чтобы удалить запись\n' +
          'Нажмите 5, чтобы изменить запись\n' +
          'Нажмите 6, чтобы выйти из меню\n')
    enter = int(input('Введите цифру от 1 до 6: '))
    if enter == 1:
        data = open('HW/8/phones.csv', 'r', encoding = 'utf-8')
        list = data.read()
        if len(list) == 0:
            print('Нет записей')
        else:
            print(list)
        data.close
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()
    elif enter == 2:
        write_in_file()
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()
    elif enter == 3:
        search()
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()
    elif enter == 4:
        rewrite(delete())
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()
    elif enter == 5:
        rewrite(change())
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()
    elif enter == 6:
        print('Программа завершила работу')
    else:
        print('Неверный ввод, введите число от 1 до 6\n')
        exit = input('Нажмите Enter, чтобы вернуться в главное меню')
        menu()

csv = exists('phones.csv')
txt = exists('phones.txt')
if not csv and not txt:
    create()
menu()
