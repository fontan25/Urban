first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:                               # Если все числа равны между собой
    print('Вывод: 3')
elif first == second or first == third or second == third: # Если хотя бы 2 из 3 введённых чисел равны между собой
    print('Вывод: 2')
else:                                                      # Если равных чисел среди 3-х вообще нет
    print('Вывод: 0')