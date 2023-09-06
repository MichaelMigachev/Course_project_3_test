# import requests

import json
import datetime

def list_operations():
   '''из json в список operations_list
      и выдаёт последние 5 операций'''
   with open('operations.json', 'r', encoding='utf-8') as file:
     operations_list = json.load(file)                            # список операций
   return operations_list[-5:]

# проверка вывод списка последних 5 операций
list_operation = list_operations()
for lists in list_operation:
   print(lists)
   if 'from' in lists:
      date_ = lists['from']
      print(date_)
   else:
       print()

def date_time(date_t):
    '''Возвращает дату в нужном формате'''
    date_t = '2018-06-29 08:15:27.243860'
    date_time_str = date_t                                # '2018-06-29 08:15:27.243860'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    today = date_time_obj.date()
    return  today.strftime("%m.%d.%Y")
date_ = '2019-01-05T00:52:30.108534'
date_ = date_.split('-')
print(date_)

print(date_time(date_))





def card_number(num):
    '''Номер карты замаскирован и не отображается целиком
     в формате  XXXX XX** **** XXXX (видны первые 6 цифр
     и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).'''

    num1_lisl = num.split()                  # переводим строку в список
    num = num1_lisl[1]                       # из списка берём второй элемент
    num_new = []                             # временный список
    for i in range(len(num)):
        if i == 4 or i == 8 or i == 12:
            num_new.append(' ')
        if 5 < i < 12:
            num_new.append('*')
        else:
            num_new.append(num[i])

    num_new = ''.join(num_new)               # собираем в новый формат вывода
    return num_new

# проверка функции по изменению номера карты
# num = 'Maestro 1308795367077170'
# print(card_number(num))

def check_number(num):
    '''Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).'''
    num1_lisl = num.split()
    num = num1_lisl[1]
    num_new = []  # временный список
    for i in range(len(num)):
        # if i == 4 or i == 8 or i == 12:
        #     num_new.append(' ')
        if  i < 16:
            num_new.append('*')
        else:
            num_new.append(num[i])

    num_new = num_new[-6:]         # берём последние 6 символов
    num_new = ''.join(num_new)     # собираем в новый формат вывода
    return num_new

# проверка функции по изменению номера счета
# num = 'Счет 46363668439560358409'
# print(check_number(num))
