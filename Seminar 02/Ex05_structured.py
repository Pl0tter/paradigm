# У нас есть отсортированный список целых чисел, и мы хотим найти
# определенное число в этом списке.
# Нам нужно реализовать функцию для поиска числа в списке.

# Отсортированный список
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target_number = 7
if target_number in sorted_numbers:
    result = sorted_numbers.index(target_number)
    print(f"Число {target_number} найдено в позиции {result}.")
else:
    print(f"Число {target_number} не найдено")
