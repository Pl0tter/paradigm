# Функция для поиска числа в отсортированном списке
def find_number_in_sorted_list(sorted_numbers, target_number):
    if target_number in sorted_numbers:
        result = sorted_numbers.index(target_number)
        return result
    else:
        return -1


# Отсортированный список чисел
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Целевое число, которое мы ищем
target_number = 7

# Вызываем функцию для поиска числа в списке
result = find_number_in_sorted_list(sorted_numbers, target_number)

# Проверяем результат и выводим сообщение
if result != -1:
    print(f"Число {target_number} найдено в позиции {result}.")
else:
    print(f"Число {target_number} не найдено в списке.")
