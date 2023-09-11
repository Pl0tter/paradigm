# Задача-1: У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды.
# Вам нужно найти это одиночное число.
# __
# Пример:
# Входной массив: [4, 3, 2, 4, 1, 3, 2]
# Результат: 1
# В данной задаче вы должны найти способ найти одиночное число с использованием массивов и алгоритмов.

def find_unique_imperative(numbers: list):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[i] == numbers[j] and i != j):
                break
            if (j == len(numbers) - 1):
                return numbers[i]
    return None


def find_unique_declarative(numbers: list):
    return list(filter(lambda x: (numbers.count(x) == 1), numbers))


numbers = [4, 3, 2, 4, 1, 3, 2]
print('Императивный стиль:')
print(find_unique_imperative(numbers))
print('Декларативный стиль:')
print(find_unique_declarative(numbers))
