# Пример структурного программирования

# Задача: Найти сумму всех чисел от 1 до N.

# Ввод данных
n = int(input("Введите число N: "))

# Инициализация переменной для хранения суммы
sum_of_numbers = 0

# Вычисление суммы
for i in range(1, n + 1):
    sum_of_numbers += i

# Вывод результата
print(f"Сумма всех чисел от 1 до {n} равна {sum_of_numbers}")

# Пример процедурного программирования
# Задача: Найти сумму всех чисел от 1 до N.
# # Функция для вычисления суммы чисел


def calculate_sum(n):
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    return sum_of_numbers

# Функция для вывода результата


def display_result(n, result):
    print(f"Сумма всех чисел от 1 до {n} равна {result}")


# Ввод данных
n = int(input("Введите число N: "))

# Вызов функций
total_sum = calculate_sum(n)
display_result(n, total_sum)
