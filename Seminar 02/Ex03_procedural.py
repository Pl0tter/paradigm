# Процедурное программирование
# Входные данные: список чисел
from random import randint


numbers = [randint(0, 10) for i in range(5)]

# Функция для вычисления среднего значения


def average(numbers):
    if len(numbers) == 0:
        return None

    average = sum(numbers) / len(numbers)
    return average


# Вычисление среднего значения с использованием функции
aver = average(numbers)

print(numbers)
print(aver)
