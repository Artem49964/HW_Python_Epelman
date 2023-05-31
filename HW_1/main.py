# # # strings
# # #
# # # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# # # наприклад:
# # st = 'as 23 fdfdg544' # введена строка
# # # # 2,3,5,4,4        #вивело в консолі.
# #
# #
# # # #################################################################################
# # # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # # так як вони написані
# # # наприклад:
# #
# #
# st = 'as 23 fdfdg544 34'
# # #   23, 544, 34              #вивело в консолі
# #

# #

# #
# # # #################################################################################
# # #
# # # list comprehension
# # #
# # # 1)є строка:
greeting = 'Hello, world'
# # # записати кожний символ як окремий елемент списку і зробити його заглавним:
# # # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# #
print([i.upper() for i in greeting])
# #
# # #
# # # 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# # # приклад:
# # # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# #
print([i ** 2 for i in range(50)])
# #
# # # function
# #
# # # - створити функцію яка виводить ліст
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def lis_printer(lis):
    print(lis)


lis_printer(l)


#
#
# #
# #
# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_printer(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


max_printer(4, 2, 1)


#
#
# #
# #
# # # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# #
def polus_printer(*args):
    print(min(*args))
    return max(*args)


#
#
# #
# #
polus_printer(3, 1, 6, 7, 8, 9, 6, -20)


#
#
# #
# #
# # # - створити функцію яка повертає найбільше число з ліста
# #
def max_in_lis(lis):
    return max(lis)


#
#
# #
# #
print(max_in_lis(l))


#
#
# #
# #
# # # - створити функцію яка повертає найменьше число з ліста
def min_in_lis(lis):
    return min(lis)


print(min_in_lis(l))


#
#
# #
# #
# # # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
def sum_of_lis(lis):
    return sum(lis)


print(sum_of_lis(l))


#
#
# #
# #
# # # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def average_of_lis(lis):
    for i in lis:
        i += i // len(lis)
    print(f'average of this list is {i}')


average_of_lis(l)

# #
# # #
# # #
# # #
# # #
# # # ################################################################################################
# # # 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# # #   - знайти мін число
print(min(list))
#
# # #   - видалити усі дублікати
print(set(list))


#
#
# # #   - замінити кожне 4-те значення на 'X'
#
# # ?
# # for e, i in enumerate(list):
# #     if e % 4 == 0:
# #         i = 'X'
# #         print(i)
# # ?
#
#
# # # 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def star(n):
    print('* ' * n)
    for i in range(n):
        print('*'[:n], ('    *'[:]))
    print('* ' * n)


star(4)
#
# # # 3) вывести табличку множення за допомогою цикла while

table_1 = 0

while table_1 < 10:
    table_1 += 1
    print(table_1, end=' ')
print('\n')

table_2 = 0

while table_2 < 20:
    table_2 += 2
    print(table_2, end=' ')
print('\n')

table_3 = 0

while table_3 < 30:
    table_3 += 3
    print(table_3, end=' ')
print('\n')

table_4 = 0

while table_4 < 40:
    table_4 += 4
    print(table_4, end=' ')
print('\n')

table_5 = 0

while table_5 < 50:
    table_5 += 5
    print(table_5, end=' ')
print('\n')

table_6 = 0

while table_6 < 60:
    table_6 += 6
    print(table_6, end=' ')
print('\n')

table_7 = 0

while table_7 < 70:
    table_7 += 7
    print(table_7, end=' ')
print('\n')

table_8 = 0

while table_8 < 80:
    table_8 += 8
    print(table_8, end=' ')
print('\n')

table_9 = 0

while table_9 < 90:
    table_9 += 9
    print(table_9, end=' ')
print('\n')

table_10 = 0

while table_10 < 100:
    table_10 += 10
    print(table_10, end=' ')
print('\n')

#
# # # 4) переробити це завдання під меню
