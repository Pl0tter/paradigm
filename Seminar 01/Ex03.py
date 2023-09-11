# Дан список чисел. Ваша задача - найти наибольшую возрастающую подпоследовательность в этом списке.

numbers = [3, 4, -1, 0, 6, 2, 3]

start = 0
number_up = []

for i in range(0, len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        stop = i + 1
    else:
        number_up.append(numbers[start:stop + 1])
        start = i + 1

number_up.append(numbers[start:stop + 1])

max_len = len(number_up[0])
max_i = 0
for i in range(len(number_up)):
    if len(number_up[i]) > max_len:
        max_i = i
print(number_up[max_i])
