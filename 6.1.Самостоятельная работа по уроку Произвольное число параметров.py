def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для хранения слов с одинаковыми корнями
    words = list(other_words)  # Преобразуем кортеж other_words в список

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])  # Если слово содержит корень или корень содержит слово, добавляем его в список same_words
    return same_words  # Возвращаем список слов с одинаковыми корнями

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')  # Вызываем функцию с аргументами
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')  # Вызываем функцию с аргументами
print(result1)  # Выводим результаты
print(result2)