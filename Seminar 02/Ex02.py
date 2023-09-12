# Пример структурного программирования

# # Входные данные: список студентов с оценками
# students = [
#     {"имя": "Анна", "оценки": [90, 85, 88]},
#     {"имя": "Петр", "оценки": [78, 92, 88]},
#     {"имя": "Мария", "оценки": [85, 87, 92]},
# ]

# # Инициализация переменных для суммы и среднего значения
# total_score = 0
# total_students = len(students)

# # Вычисление суммы оценок
# for student in students:
#     total_score += sum(student["оценки"])

# # Вычисление среднего балла
# average_score = total_score / (total_students * len(students[0]["оценки"]))

# # Вывод результата
# print(f"Средний балл студентов: {average_score:.2f}")


# Пример процедурного программирования

# Функция для вычисления среднего балла студента
def calculate_average(scores):
    return sum(scores) / len(scores)

# Функция для вычисления среднего балла всех студентов


def calculate_class_average(students):
    total_score = 0
    total_students = len(students)

    for student in students:
        total_score += calculate_average(student["оценки"])

    return total_score / total_students


# Входные данные: список студентов с оценками
students = [
    {"имя": "Анна", "оценки": [90, 85, 88]},
    {"имя": "Петр", "оценки": [78, 92, 88]},
    {"имя": "Мария", "оценки": [85, 87, 92]},
]

# Вычисление среднего балла
average_score = calculate_class_average(students)

# Вывод результата
print(f"Средний балл студентов: {average_score:.2f}")
