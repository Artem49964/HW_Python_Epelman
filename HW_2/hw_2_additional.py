# 2.1
# вивести послідовність Фібоначі, кількість вказана в знінній,
#  наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#  (число з послідовності - це сума попередніх двох чисел)

def subsequence_fibonachi() -> None:
    f1 = 1
    f2 = 1
    # Перші 2 числа нам вже відомі, тому кількість ітерацій буде i - 2

    num = int(input('Введіть число, рівне ряду послідовності: '))
    # Просимо користувача ввести число

    for i in range(2, num):
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')
        num -= 1

# subsequence_fibonachi()


########################################################################################################################################



# 2.2
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#    х = 33294 -> п = 2, н = 3

def counter_even_odd_nums():
    num = int(input('Введіть число для підрахунку парності/непарності: '))
    choise_even_odd = int(input('Підрахувати парні чи непарні числа?\n 1 - Непарні.\n 2 - Парні.\n'))
    if choise_even_odd == 1:
        odd_nums = [i for i in range(num) if i % 2 != 0]
        print(f'{odd_nums}')
    elif choise_even_odd == 2:
        even_nums = [i for i in range(num) if i % 2 == 0]
        print(f'{even_nums}')


# counter_even_odd_nums()


# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3



#######################################################################################################################################


# 2.3
# прога, що виводить кількість кожного символа з введеної строки

# наприклад:
# 'a' -> 1  # вивело в консолі
#  's' -> 1

# прога, що виводить кількість кожного символа з введеної строки

# наприклад:
st = 'as 23 fdfdg544'  # введена строка

# 'a' -> 1  # вивело в консолі
# 's' -> 1

# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2


st = 'as 23 fdfdg544'  # введена строка

def count_of_item(arg: list, item: str) -> str:
    for i in arg:
        return f'"{item}" -> {arg.count(item)}'


# print(count_of_item(st, '4'))



#######################################################################################################################################

# 2.4
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:

#######################################################################################################################################


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]


lis = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# В РОБОТІ
# def num_list_generator(arg: list):
#     for i in arg:
#         main_list = []
# print(num_list_generator(lis))

#######################################################################################################################################


# 2.5 найти со списка только уникальные числа
# l = [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

l = [1, 2, 3, 4, 2, 5, 1]
s = list(set(l))
# print(s)
#######################################################################################################################################


