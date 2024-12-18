def calculate_structure_sum(arg):
    total = 0

    if isinstance(arg, int ):
        total += arg # Если элемент - число, добавляем его к сумме
    elif isinstance(arg, str):
        total += len(arg) # Если элемент - строка, добавляем её длину к сумме
    elif isinstance(arg, (list, tuple, set)): # Если элемент - список, кортеж или множество, рекурсивно обрабатываем каждый элемент
        for element in arg:
            total += calculate_structure_sum(element)
    elif isinstance(arg, dict): # Если элемент - словарь, рекурсивно обрабатываем ключи и значения
        for key, value in arg.items():
            total = total + calculate_structure_sum(value) + calculate_structure_sum(key)
    return total

data_structure = [[1,2,3],{'a':4,'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2,'Urban',('Urban2',35))}])]

result = calculate_structure_sum(data_structure)
print(result)