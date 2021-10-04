"""
Напишите функцию, которая находит сумму четных элементов на главной диагонали
квадратной матрицы (именно чётных элементов, а не элементов на чётных позициях!).
Если чётных элементов нет, то вывести 0. Используйте библиотеку numpy.
"""

import numpy as np


def diag_2k(a):
    #param a: np.array[size, size]

    result = sum(e for e in np.diag(a) if e % 2 == 0)
    return result

a = np.arange(9).reshape(3, 3)
print(a)
print(diag_2k(a))
