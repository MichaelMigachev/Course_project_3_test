from functions import list_operations, date_time, card_number,check_number


list_operation = []                             # списка последних 5 операций
list_operation = list_operations()              # получение списка последних 5 операций

list_date = []                                  # список дат операций
for i in range(len(list_operation)):            # создание списка дат
    list_date.append(list_operation[i]["date"])

for j in range(len(list_date)):
    max_date = max(list_date)
    for i in range(len(list_operation)):
        if list_operation[i]["date"] == max_date:
            # print(list_operation[i])
            # dict1 = list_operation[i]
            print(f'{date_time(list_operation[i]["date"])} {list_operation[i]["description"]}')


            if "from" in list_operation[i]:
                if "Счет" in list_operation[i]["from"]:
                    print(f'{check_number(list_operation[i]["from"])} -> {check_number(list_operation[i]["to"])}')
                else:
                    print(f'{card_number(list_operation[i]["from"])} -> {check_number(list_operation[i]["to"])}')
            else:
                print(check_number(list_operation[i]["to"]))

            print(f'{list_operation[i]["operationAmount"]["amount"]}')
            list_date.remove(max(list_date))
            print()
