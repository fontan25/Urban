def get_multiplied_digits(number):
    number_str = str(number)               # Преобразуем число в строку
    product = 1                            # Инициализируем переменную для хранения произведения

    for digit in number_str:               # Проходим по каждой цифре в строке
        if digit != '0':                   # Если цифра не равна нулю,
            product *= int(digit)          # умножаем ее на текущее значение произведения
    return product                         # Возвращаем произведение цифр

print(get_multiplied_digits(40203))   # Выведет: 24
print(get_multiplied_digits(402030))  # Выведет: 24
