# Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива.
# Одно из чисел в массиве повторяется дважды, а одно число пропущено. Найдите повторяющееся число и пропущенное число.
# __
# Пример:
# Входной массив: [2, 3, 1, 5, 3]
# Повторяющееся число: 3
# Пропущенное число: 4


def find_numbers_imperative(numbers: list):
    counter = {}
    for i in range(1, len(numbers) + 1):
        counter[i] = 0

    for j in range(len(numbers)):
        counter[numbers[j]] += 1

    for key, value in counter.items():
        if (value == 0):
            absent = key
        if (value == 2):
            dbl = key

    return dbl, absent


numbers = [2, 3, 1, 5, 3]

print(
    f'Повторяющееся число: {find_numbers_imperative(numbers)[0]}\nПропущенное число: {find_numbers_imperative(numbers)[1]}')
