# функцию расчета скидки на покупку, в зависимости от следующих условий:
# Если общая сумма покупки больше или равна 1000 рублей, то скидка составляет 10%.
# Если общая сумма покупки больше или равна 500 рублей, то скидка составляет 5%.
# В остальных случаях скидки нет.

discount = 0
total = 1200

if total >= 1000:
    discount = total * 0.1
elif total >= 500:
    discount = total * 0.05
else:
    discount = 0

print(discount)