# 1)
# Создайте структуру с именем train, содержащую поля: название пункта назначения, номер поезда,
# время отправления. +

# Ввести данные в массив из пяти элементов типа train +

# упорядочить элементы по номерам поездов +

# Добавить возможность вывода информации о поезде номер которого введен пользователем.

# Добавить возможность сортировки массив по пункту назначения, причем поезда с одинаковыми пунктами назначения должны быть упорядочены по

# времени отправления.


class Train():
    def __init__(self, point_departure: str, point_use: str, train_number: int, time_departure: str, time_use: str):
        self.point_departure = point_departure
        self.point_use = point_use
        self.train_number = train_number
        self.time_departure = time_departure
        self.time_use = time_use

    def __str__(self):
        return f'\nСполучення: {self.point_departure} - {self.point_use}\nНомер потяга - {self.train_number}\nЧас відправлення - {self.time_departure}\nЧас прибуття - {self.time_use}\n'


trains: list[Train] = [
    Train('Odessa', 'Kyiv', 20, '20.00', '08.00'),
    Train('Lviv', 'Odessa', 38, '15.20', '09.20'),
    Train('Sumy', 'Lviv', 10, '00.20', '03.20'),
    Train('Izmail', 'Sevastopol', 2, '09.30', '20.30'),
    Train('Fastov', 'Kyiv', 87, '06.40', '10.30')
]#.sort(key=lambda x: x.train_number) - намагався відсортувати на місці


sorted_trains = sorted(trains, key=lambda x: x.train_number)

# for train in sorted_trains:
#     print(train)

choise_train = int(input('Введіть номер потяга, будь-ласка: '))

for train in sorted_trains:
    if choise_train == train.train_number:
        print(train)



def sorting_by_point_use(arg:list):
    for i in trains:

        sorted_trains = sorted(trains, key=lambda x: x.point_use[0])
        sorted_trains_time_use = sorted(trains, key=lambda x: x.time_use[0])








# 2)
# Построить три класса (базовый и 3 потомка), описывающих некоторых хищных животных (один из потомков),
# всеядных(второй потомок) и травоядных (третий потомок). Описать в базовом классе абстрактный метод для расчета количества и типа
# пищи, необходимого для пропитания животного в зоопарке.
# a) Упорядочить всю последовательность животных по убыванию количества пищи. При совпадении значений – упорядочивать
# данные по алфавиту по имени. Вывести идентификатор животного, имя, тип и количество потребляемой пищи для всех элементов списка.
# b) Вывести первые 5 имен животных из полученного в пункте а) списка.
# c) Вывести последние 3 идентификатора животных из полученного в пункте а) списка.
# d) Организовать запись и чтение коллекции в/из файл.
# e) Организовать обработку некорректного формата входного файла.
