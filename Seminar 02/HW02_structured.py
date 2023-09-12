# Задача 1
# __
# Допустим, у нас есть задача по обработке данных о студентах в университете. У нас есть следующие данные:
# __
# Список студентов с их именами и оценками.
# Нам нужно найти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего.
# Сделать 2 варианта решения, т.е. реализация структурного программирования и процедурного программирования

# Список студентов

student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]

total_score = 0
total_students = 0

for student in student_data:
    total_score += student["score"]
    total_students += 1

average = total_score / total_students

above_average_students = []

for student in student_data:
    if (student["score"] > average):
        above_average_students.append(student["name"])

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")
