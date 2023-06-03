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
def expanded_form(arg) -> str:
    for i in range(arg):
        if arg < 100:
            return f'{str(arg)[0]}{0} + {str(arg)[1]}'
        elif arg >= 100 and arg < 1000:
            return f'{str(arg)[0]}{"0" * 2} + {str(arg)[1]}{0} + {str(arg)[2]}'
        elif arg >= 1000 and arg < 10000:
            return f'{str(arg)[0]}{"0" * 3} + {str(arg)[1]}{"0" * 2} + {str(arg)[2]}{0} + {str(arg)[3]}'
        elif arg >= 10000 and arg < 100000:
            return f'{str(arg)[0]}{"0" * 4} + {str(arg)[1]}{"0" * 3} + {str(arg)[2]}{"0" * 2} + {str(arg)[3]}{"0"} + {str(arg)[4]}'
        elif arg >= 100000 and arg < 1000000:
            return f'{str(arg)[0]}{"0" * 5} + {str(arg)[1]}{"0" * 4} + {str(arg)[2]}{"0" * 3} + {str(arg)[3]}{"0" * 2} + {str(arg)[4]}{"0"} + {str(arg)[5]}'
        elif arg >= 1000000 and arg < 10000000:
            return f'{str(arg)[0]}{"0" * 6} + {str(arg)[1]}{"0" * 5} + {str(arg)[2]}{"0" * 4} + {str(arg)[3]}{"0" * 3} + {str(arg)[4]}{"0" * 2} + {str(arg)[5]}{"0"} + {str(arg)[6]}'


# Функція працює з дефектом: Корректно розкладає число на розряди, якщо в числі немає цифри 0
# питання: Як поставити перевірку - Якщо str(arg)[i] == 0: pass


print(expanded_form(22))
print(expanded_form(233))
print(expanded_form(2034))
print(expanded_form(26345))
print(expanded_form(233456))
print(expanded_form(2234567))


# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
#
#
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим
# декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    counter = 0

    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        func(*args, **kwargs)
        print(counter)

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
