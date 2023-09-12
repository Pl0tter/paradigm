# У вас есть список чисел, и вам нужно вычислить среднее значение этого списка чисел.

from random import randint
# Входные данные: список чисел
numbers = [randint(0, 10) for i in range(5)]

# Инициализация переменных для суммы и количества чисел
summ = 0
count = 0
# Вычисление суммы чисел и их количества
for number in numbers:
    summ += number
    count += 1
# Вычисление среднего значения
average = summ / count

print(numbers)
print(average)
