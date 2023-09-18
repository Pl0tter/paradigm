# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.

from functools import reduce
from random import randint


def correlation_coefficient(abscissa: list, ordinate: list):

    dev_X = list(map(lambda x: x - sum(abscissa)/len(abscissa), abscissa))

    dev_Y = list(map(lambda y: y - sum(ordinate)/len(ordinate), ordinate))
    numerator = reduce(lambda x, y: x + y,
                       [dev_X[i] * dev_Y[i] for i in range(len(dev_X))])
    denominator = reduce(
        lambda x, y: x + y, [dev_X[i]**2 * dev_Y[i]**2 for i in range(len(dev_X))])**0.5
    return numerator/denominator


abscissa = [randint(0, 10) for i in range(10)]
ordinate = [randint(0, 10) for i in range(10)]
print(f"X: {abscissa}")
print(f"Y: {ordinate}")

print(correlation_coefficient(abscissa, ordinate))
