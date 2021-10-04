"""На вход дан двумерный массив XXX. Напишите функцию, которая
для каждой строчки x=(x1,x2,…,xn) массива X
строит строчку s=(s1,s2,…,sn), где
sk=x1+...+xk, а затем выдаёт массив из построенных строчек.
Используйте библиотеку numpy (вам поможет функция cumsum).
Выходом функции должен быть двумерный массив той же формы, что и X."""

import numpy as np

def cumsum(A):
    #param A: np.array[m,n]

    result = np.cumsum(A, axis=1)
    return result

A = np.arange(10).reshape(2, 5)
print(A)
print(cumsum((A)))
