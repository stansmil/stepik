"""Вам подаются на вход два вектора a и b в трехмерном пространстве.
Реализуйте их скалярное произведение с помощью numpy и без. """

import numpy as np

def no_numpy_scalar(v1, v2):
    #param v1, v2: lists of 3 ints
    #YOUR CODE: please do not use numpy

    result = sum(a * b for a, b in zip(v1, v2))
    return result

def numpy_scalar (v1, v2):
    #param v1, v2: np.arrays[3]

    result = v1.dot(v2)
    return result


v1 = [1,2,3]
v2 = [3,2,1]
print(no_numpy_scalar(v1, v2))

v1 = np.array(v1)
v2 = np.array(v2)
print(numpy_scalar(v1, v2))
