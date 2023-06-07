# # Створити клас Rectangle:
# # -він має приймати дві сторони x,y
# # -описати поведінку на арифметични методи:
# #   + сумма площин двох екземплярів ксласу
# #   - різниця площин двох екземплярів ксласу
# #   == площин на рівність
# #   != площин на не рівність
# #   >, < меньше більше
# #   при виклику метода len() підраховувати сумму сторін

from abc import ABC


class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (self.a + self.b) * 2

    def __mod__(self, other):
        return self.a == self.b

    def __eq__(self, other):
        return self.a == self.b

    def __ne__(self, other):
        return self.a != self.b

    def __gt__(self, other):
        return self.a > self.b

    def __lt__(self, other):
        return self.a < self.b

    def __len__(self):
        return len(Rectangle)


# ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення




class Human(ABC):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @name.deleter
    def name(self) -> None:
        del self.__name

    @age.setter
    def age(self, age: str) -> None:
        self.__age = age

    @age.deleter
    def age(self) -> None:
        del self.__age


class Cinderella(Human):
    __instance = None
    count = 0

    # def __new__(cls, *args, **kwargs):
    #     if not isinstance(cls.__instance, cls):
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __init__(self, name: str, age: int, leg_size: int):
        super().__init__(name, age)
        self.leg_size = leg_size
        Cinderella.count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.count


cinderellas: list[Cinderella] = [Cinderella('Cindy', 18, 39), Cinderella('Izabella', 20, 38),
                                 Cinderella('Anaconda', 40, 45)]

print(cinderellas[1].leg_size)


class Prince(Human):
    def __init__(self, name, age, found_shoe):
        super().__init__(name, age)
        self.found_shoe = found_shoe

    @property
    def shoe(self):
        return self.found_shoe

    def founding_shoe(cls, cinderellas_list):
        for i in cinderellas_list:
            if cls.found_shoe == i.leg_size:
                print(f'{i.name}, {i.age}, {i.leg_size} is she!')


char = Prince('Charming', 20, 38)
char.founding_shoe(cinderellas)


###############################################################################


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

class Printable(ABC):
    def __init__(self):
        pass

    def printer(*args, **kwargs) -> None:
        print(*args, **kwargs)

    def __str__(self):
        return str()


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Magazine(Printable):
    def __init__(self, name):
        super().__init__()
        self.name = name


# 3) Створити клас Main в якому буде:

# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Main(Printable):
    printable_list = []

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, value):
        if isinstance(value, Book) or isinstance(value, Magazine):
            cls.printable_list.append(value)
        else:
            pass

    @classmethod
    def show_all_magazines(cls):
        for i in cls.printable_list:
            if isinstance(i, Magazine):
                cls.printer(i.name)
            else:
                pass


    @classmethod
    def show_all_books(cls):
        for i in cls.printable_list:
            if isinstance(i, Book):
                cls.printer(i.name)
            else:
                pass




Main.add(Magazine('Magazine1'))
Main.show_all_magazines()
Main.add(Book('Book1'))
Main.show_all_books()


# Приклад:
#

# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для
# перевірки
# ксассів
# використовуємо
# метод
# isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
