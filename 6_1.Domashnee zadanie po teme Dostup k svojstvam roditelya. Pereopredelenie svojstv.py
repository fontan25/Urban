class Vehicle:  # Создаем класс Vehicle
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Список допустимых цветов для окрашивания

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Устанавливаем владельца транспорта
        self.__model = model  # Устанавливаем модель транспорта
        self.__engine_power = engine_power  # Устанавливаем мощность двигателя
        self.__color = color  # Устанавливаем цвет транспорта

    def get_model(self):
        return f"Модель: {self.__model}"  # Возвращаем модель транспорта

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"  # Возвращаем мощность двигателя

    def get_color(self):
        return f"Цвет: {self.__color}"  # Возвращаем цвет транспорта

    def print_info(self):
        print('\033[34m', self.get_model())  # Выводим модель транспорта
        print(self.get_horsepower())  # Выводим мощность двигателя
        print(self.get_color())  # Выводим цвет транспорта
        print('Владелец:', self.owner)  # Выводим владельца транспорта

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:  # Если новый цвет есть в списке допустимых цветов
            self.__color = new_color  # Меняем цвет транспорта на новый
        else:
            print(f'\033[37mНельзя сменить цвет на {new_color}')  # Выводим сообщение об ошибке


class Sedan(Vehicle):  # Создаем класс Sedan, унаследованный от Vehicle
    __PASSENGERS_LIMIT = 5  # Ограничение на количество пассажиров


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)  # Создаем объект класса Sedan

# Изначальные свойства
vehicle1.print_info()  # Выводим информацию о транспорте

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # Пытаемся изменить цвет на 'Pink'
vehicle1.set_color('BLACK')  # Пытаемся изменить цвет на 'BLACK'
vehicle1.owner = 'Vasyok'  # Меняем владельца транспорта

# Проверяем что поменялось
vehicle1.print_info()  # Выводим информацию о транспорте