# Императивный код для нахождения суммы чисел от 0 до n
def sum_up_to_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

# Декларативный запрос для выборки имен и возрастов
# SELECT name, age FROM users WHERE age > 25;

# Декларативный код для нахождения суммы чисел от 0 до n с использованием функционального стиля


def sum_up_to_n_declarative(n):
    return sum(range(1, n+1))
