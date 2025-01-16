import random

class Animal:  # Создаем класс Animal
    live = True  # Живой
    sound = None  # Звук
    _DEGREE_OF_DANGER = 0  # Степень опасности

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты
        self.speed = speed  # Скорость

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed  # Новая координата X
        new_y = self._cords[1] + dy * self.speed  # Новая координата Y
        new_z = self._cords[2] + dz * self.speed  # Новая координата Z
        if new_z < 0:
            print("It's too deep, i can't dive :(")  # Выводим сообщение об ошибке, если глубина слишком большая
        else:
            self._cords = [new_x, new_y, new_z]  # Обновляем координаты

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')  # Выводим координаты

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:  # Если степень опасности меньше 5
            print("Sorry, i'm peaceful :)")  # Выводим сообщение о том, что животное мирное
        else:
            print("Be careful, i'm attacking you 0_0")  # Выводим сообщение о том, что животное атакует

class Bird(Animal):  # Создаем класс Bird, унаследованный от Animal
    beak = True  # Клюв есть

    def lay_eggs(self):
        num_of_eggs = random.randint(1, 4)  # Генерируем случайное количество яиц
        print(f"Here are(is) {num_of_eggs} eggs for you")  # Выводим количество яиц

class AquaticAnimal(Animal):  # Создаем класс AquaticAnimal, унаследованный от Animal
    _DEGREE_OF_DANGER = 3  # Степень опасности

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz) * 5 * self.speed  # Новая координата Z
        self._cords[2] = max(new_z, 0)  # Обновляем координату Z

class PoisonousAnimal(Animal):  # Создаем класс PoisonousAnimal, унаследованный от Animal
    _DEGREE_OF_DANGER = 8  # Степень опасности

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):  # Создаем класс Duckbill, унаследованный от PoisonousAnimal,
    # Bird и AquaticAnimal
    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed):
        super().__init__(speed)  # Инициализируем класс Animal

    def speak(self):
        print(self.sound)  # Выводим звук утконоса

db = Duckbill(10)  # Создаем объект класса Duckbill

print(db.live)  # Выводим значение атрибута live
print(db.beak)  # Выводим значение атрибута beak

db.speak()  # Выводим звук утконоса
db.attack()  # Выводим сообщение о том, атакует ли утконос

db.move(1, 2, 3)  # Перемещаем утконоса
db.get_cords()  # Выводим координаты утконоса
db.dive_in(6)  # Погружаем утконоса
db.get_cords()  # Выводим координаты утконоса

db.lay_eggs()  # Выводим количество яиц, которые может отложить утконос