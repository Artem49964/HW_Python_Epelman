# 1)написати функцію на замикання котра буде в собі зберігати список справ,
# вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from typing import Callable

from typing import Any


def notebook() -> Callable[[str], Any]:
    todo_list = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)
        if todo == False:
            print(f'"{todo}" is appended in list')

    def get_all() -> list:
        nonlocal todo_list
        return todo_list

    def delete_todo() -> None:
        nonlocal todo_list
        choise_of_del = str(input(f'Оберіть справу для видалення з списку нижче:\n{todo_list}'))
        if choise_of_del == choise_of_del:
            todo_list.remove(choise_of_del)
        else:
            print('Справа введена не корректно')

    return add_todo, get_all, delete_todo


add_todo, get_all, delete_todo = notebook()


# 2) протипізувати перше завдання


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
# def expanded_form(arg: int):


# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
#
#
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим
# декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    count_of_call = 0

    def inner():
        nonlocal count_of_call
        count_of_call += 1
        print(count_of_call)

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()

func2()
func2()
