# 1) Є ось такий файл... ваша задача записати в новий файл тільки emailʼли з доменом gmail.com (Хеш то що з ліва
# записувати не потрібно)

import json

try:
    with open('emailes.txt', 'r') as email, open('gmails.txt', 'w') as gmail:
        for i in email:
            if '@gmail.com' in i:
                gmail.write(f'{str(i[35:-1])}\n')
except Exception as err:
    print(err)


########################################################################################################################


# 2) Створити записну книжку покупок: +
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі

class Buy:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price


purches = []

try:
    with open('purches.json', 'w') as buy:
        json.dump(purches, buy)
except Exception as err:
    print(err)


# з функціоналу:

####################################################
 # * вивід всіх покупок +

def purche_getter():
    try:
        with open('purches.json', 'r+') as buy:
            all_purches = json.load(buy)
            for i in all_purches:
                print(i)
    except Exception as err:
        print(err)
# purche_getter()

####################################################

#  * має бути змога додавати покупку в книгу +

def purche_setter(arg:[Buy]):
    try:
        with open('purches.json', 'w') as buy:
            new_buy = purches.append(arg.__dict__)
            json.dump(purches, buy)
    except Exception as err:
        print(err)
#
#

purche_setter(Buy(1, 'juice', 31))
purche_setter(Buy(2, 'apple', 9.3))
purche_setter(Buy(3, 'tea', 10))
purche_setter(Buy(4, 'tomato', 20))
purche_setter(Buy(5, 'milk', 18))
purche_setter(Buy(6, 'iphone', 100))
purche_setter(Buy(7, 'dron', 23270))


# purche_getter() # чудово

####################################################
# * має бути змога шукати по будь якому полю покупку - (Дізнатись як та використати matcher pattern)

def purche_founder():
    try:
        with open('purches.json', 'r') as buy:
            print('1. id\n2. name\n3. price')
            lis = json.load(buy)
            choose_field = int(input('По якому полю ви хотіли б шукати покупку? Оберіть цифру з варіантів вище: '))
            if choose_field == 1:
                choose_field_id = str(input('Оберіть порядковий номер покупки: '))

            elif choose_field == 2:
                choose_field_name = str(input('Оберіть назву покупки: '))

            elif choose_field == 3:
                choose_field_price = str(input('Оберіть ціну покупки: '))
            for i in lis:
                print(i)
                if choose_field_name == i['name3']:
                    print(i)
                if choose_field_id == i['id']:
                    print(i)
                if choose_field_price == i['price']:
                    print(i)



    except Exception as err:
        print(err)
#
# purche_founder()


####################################################
# * має бути змога показати найдорожчу покупку +

def most_expensive_buy():
    try:
        with open('purches.json') as file:
            parsed_file = json.load(file)
            lis = list(parsed_file)
            lis.sort(key=lambda x:x['price'])
            print(lis[-1])

    except Exception as err:
        print(err)


# most_expensive_buy()


####################################################
# * має бути можливість видаляти покупку по id - (доробити)

def id_deleter():
    try:
        with open('purches.json', 'r+') as file:
            deleter_choiser = int(input('Выберите id, пo которому хотите удалить файл: '))
            parsed_file = json.load(file)
            for n, i in enumerate(parsed_file):
                if deleter_choiser == i['id']:
                    del parsed_file[n]
            json.dump(parsed_file, file)


    except Exception as err:
        print(err)


# id_deleter()

####################################################
# (ну і меню на це все) -

def menu():
    print('1.Вивід всіх покупок\n2.Додати покупку в книгу\n3.Знайти покупку по полю\n4.Показати найдорожчу покупку\n5.Видалити покупку по id')

    choise = int(input("Оберіть номер функції зі списку вище: "))

    if choise == 1:
        purche_getter()
    elif choise == 2:
        instance = input('Пропишіть екземпляр классу Buy: ')
        purche_setter(instance)
    elif choise == 3:
        purche_founder()
    elif choise == 4:
        most_expensive_buy()
    elif choise == 5:
        id_deleter()

menu()


########################################################################################################################


# 3) Кому буде замало ось завдання з співбесіди
# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]










