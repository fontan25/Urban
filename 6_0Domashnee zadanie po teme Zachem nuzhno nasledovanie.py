class Animal:  # Создаем родительский класс животные
    alive = True  # (живой)
    fed = False  # (накормленный)

    def __init__(self, name):
        self.name = name  # Устанавливаем имя животного


class Plant:  # Создаем родительский класс растений
    edible = False  # (съедобность)

    def __init__(self, name):
        self.name = name  # Устанавливаем имя растения


class Mammal(Animal):  # Создаем унаследованный класс животных - Травоядные
    def eat(self, food):
        if food.edible:  # Если растение съедобно
            print(f'{self.name} съел {food.name}')  # Выводим сообщение о том, что животное съело растение
            self.fed = True  # Устанавливаем флаг накормленности в True
        else:
            print(f'{self.name} не стал есть {food.name}')  # Выводим сообщение о том, что животное не съело растение
            self.alive = False  # Устанавливаем флаг живого в False


class Predator(Animal):  # Создаем унаследованный класс животных - Хищники
    def eat(self, food):
        if food.edible:  # Если растение съедобно
            print(f'{self.name} съел {food.name}')  # Выводим сообщение о том, что животное съело растение
            self.fed = True  # Устанавливаем флаг накормленности в True
        else:
            print(f'{self.name} не стал есть {food.name}')  # Выводим сообщение о том, что животное не съело растение
            self.alive = False  # Устанавливаем флаг живого в False


class Flower(Plant):  # Унаследованный класс растений - Цветы
    pass  # edible = True


class Fruit(Plant):  # Унаследованный класс растений - Фрукты
    edible = True  # Устанавливаем флаг съедобности в True


# Ввод названий животных и растений
animal1 = Predator('Волк с Уолл-Стрит')  # Создаем объект класса Predator
animal2 = Mammal('Хатико')  # Создаем объект класса Mammal
plant1 = Plant('Цветик семицветик')  # Создаем объект класса Plant
plant2 = Fruit('Заводной апельсин')  # Создаем объект класса Fruit

# Вывод результата
print(animal1.name)  # Выводим имя животного
print(plant1.name)  # Выводим имя растения

print(animal1.alive)  # Выводим флаг живого животного
print(animal2.fed)  # Выводим флаг накормленности животного

animal1.eat(plant1)  # Пытаемся накормить животное растением
animal2.eat(plant2)  # Пытаемся накормить животное растением
print(animal1.alive)  # Выводим флаг живого животного
print(animal2.fed)  # Выводим флаг накормленности животного
