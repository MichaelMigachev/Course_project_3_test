# import requests

import json
import datetime

file_name = 'operations.json'
def list_operations(file_name):
   '''из json в список операций operations_list и выдаёт последние 5 операций'''

   list_5_operation = []  # список последних 5 операций
   list_date = []         # список дат операций

   with open(file_name, 'r', encoding='utf-8') as file:
     operations_list = json.load(file)                            # список операций

     for i in range(len(operations_list)):            # создание списка дат
        if "date" in operations_list[i]:
            list_date.append(operations_list[i]["date"])

    # список дат по возрастанию
   list_date_ascending = []                         # список дат операций по возрастанию
   for j in range(len(list_date)):
        max_date = max(list_date)
        for i in range(len(list_date)):
            if list_date[i] == max_date:
                 list_date_ascending.append(max_date)
                 list_date.remove(list_date[i])
                 break
   list_date_ascending = list_date_ascending[:5]
# получение списка последних 5 операций
   for j in range(len(list_date_ascending)):
        for i in range(len(operations_list)):
            if list_date_ascending[j] == operations_list[i]["date"]:
                list_5_operation.append(operations_list[i])
                break
   return list_5_operation


def date_time(date_t):
    '''Возвращает дату в нужном формате'''
    # date_t = '2018-06-29 08:15:27.243860'
    date_1 = list(date_t)
    date_1[10] = ' '
    date_t = ''.join(date_1)
    date_time_str = date_t                                # '2018-06-29 08:15:27.243860'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    today = date_time_obj.date()
    return  today.strftime("%m.%d.%Y")




def card_number(num):
    '''Номер карты замаскирован и не отображается целиком
     в формате  XXXX XX** **** XXXX (видны первые 6 цифр
     и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).'''

    num1_lisl = num.split()                  # переводим строку в список
    num = num1_lisl[-1]                      # из списка берём второй элемент
    num_new = []                             # временный список
    for i in range(len(num)):
        if i == 4 or i == 8 or i == 12:
            num_new.append(' ')
        if 5 < i < 12:
            num_new.append('*')
        else:
            num_new.append(num[i])
    # собираем в новый формат вывода
    num1_lisl[-1] = ''.join(num_new)
    num_new = ' '.join(num1_lisl)
    return num_new


def check_number(num):
    '''Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).'''
    num1_lisl = num.split()
    num = num1_lisl[1]
    num_new = []  # временный список
    for i in range(len(num)):
        if  i < 16:
            num_new.append('*')
        else:
            num_new.append(num[i])

    num_new = num_new[-6:]         # берём последние 6 символов
    num_new = num1_lisl[0] + ' ' + ''.join(num_new)     # собираем в новый формат вывода
    return num_new


def final_list():
    ''' вывод последних 5 операций в нужном формате'''
    list_operation = []  # список последних 5 операций
    list_operation = list_operations(file_name)  # получение списка последних 5 операций

    for i in range(len(list_operation)):
        print(f'{date_time(list_operation[i]["date"])} {list_operation[i]["description"]}')
        if "from" not in list_operation[i]:
            print(check_number(list_operation[i]["to"]))
        if "from" in list_operation[i]:
            if "Счет" not in list_operation[i]["to"]:
                print(f'{card_number(list_operation[i]["from"])} -> {card_number(list_operation[i]["to"])}')
            else:
                if "Счет" in list_operation[i]["from"]:
                    print(f'{check_number(list_operation[i]["from"])} -> {check_number(list_operation[i]["to"])}')
                else:
                    print(f'{card_number(list_operation[i]["from"])} -> {check_number(list_operation[i]["to"])}')

        print(f'{list_operation[i]["operationAmount"]["amount"]} '
              f'{list_operation[i]["operationAmount"]["currency"]["name"]}')

        print()

    return ''
