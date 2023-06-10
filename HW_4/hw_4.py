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


purches = [
    Buy(1, 'milk', 18).__dict__,
    Buy(2, 'tomato', 20).__dict__,
    Buy(3, 'tea', 10).__dict__,
    Buy(4, 'apple', 9.3).__dict__,
    Buy(5, 'juice', 31).__dict__,
]

try:
    with open('purches.json', 'w') as buy:
        json.dump(purches, buy)
except Exception as err:
    print(err)


# з функціоналу:

####################################################
#  * вивід всіх покупок +

# def purche_getter():
#     try:
#         with open('purches.json', 'r') as buy:
#             all_purches = json.load(buy)
#             print(all_purches)
#     except Exception as err:
#         print(err)


# purche_getter()

####################################################

#  * має бути змога додавати покупку в книгу +

# def purche_setter(arg: dict[Buy]):
#     try:
#         with open('purches.json', 'w') as buy:
#             new_buy = purches.append(arg.__dict__)
#             json.dump(purches, buy)
#     except Exception as err:
#         print(err)


# purche_setter(Buy(6, 'iphone', 100))
# purche_setter(Buy(7, 'dron', 23270))
# purche_getter() # чудово

####################################################

# * має бути змога шукати по будь якому полю покупку -

# def purche_founder():
#     try:
#         with open('purches.json', 'r') as buy:
#             print('1. id\n2. name\n3. price')
#             lis = json.load(buy)
#             choose_field = int(input('По якому полю ви хотіли б шукати покупку? Оберіть цифру з варіантів вище: '))
#
#             if choose_field == 1:
#                 choose_field_id = str(input('Оберіть порядковий номер покупки: '))
#
#             elif choose_field == 2:
#                 choose_field_name = str(input('Оберіть назву покупки: '))
#
#             elif choose_field == 3:
#                 choose_field_price = str(input('Оберіть ціну покупки: '))
#             for i in lis:
#                 if choose_field_name in i['name']:
#                     print(i)
#
#                 # if choose_field_id in i['name']:
#                 #     print(i)
#                 # if choose_field in str(i['id']):
#
#                 # else:
#                 #     pass
#
#     except Exception as err:
#         print(err)

# purche_founder()


####################################################
# * має бути змога показати найдорожчу покупку -

# def most_expensive_buy():
#     try:
#         with open('purches.json') as file:
#             parsed_file = json.load(file)
#             lis = list(parsed_file)
#             lis.sort(key=lambda x:x['price'])
#             print(lis[-1])
#
#     except Exception as err:
#         print(err)
#
#
# most_expensive_buy()



####################################################
# * має бути можливість видаляти покупку по id -


####################################################
# (ну і меню на це все) -


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
