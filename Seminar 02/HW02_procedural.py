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


def find_average(students: list):
    total_score = 0
    for student in students:
        total_score += student["score"]
    return total_score / len(students)


def above_average(students: list, average):
    above_average_list = []
    for student in students:
        if (student["score"] > average):
            above_average_list.append(student["name"])
    return above_average_list


average = find_average(student_data)
above_average_students = above_average(student_data, average)

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")
