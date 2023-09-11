# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

from random import randint


def sort_list_imperative(numbers: list):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] < numbers[j]):
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def sort_list_declarative(numbers: list):
    numbers.sort(reverse=True)
    return numbers


numbers = [randint(0, 10) for i in range(10)]
print(numbers)
print('Императивный стиль:')
print(sort_list_imperative(numbers))
print('Декларативный стиль:')
print(sort_list_declarative(numbers))
