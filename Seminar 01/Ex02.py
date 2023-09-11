# Напишите программу, которая находит сумму всех четных чисел от 1 до 100 с использованием императивного (структурного) программирования (цикла).

start = 1
stop = 100
summ = 0

# Вариант 1
for i in range(start, stop + 1):
    if i % 2 == 0:
        summ += i
print(summ)

# Вариант 2
even_numbers = [num for num in range(start, stop + 1) if num % 2 == 0]
print(sum(even_numbers))

# Декларативный стиль
print(sum(range(0, 101, 2)))
