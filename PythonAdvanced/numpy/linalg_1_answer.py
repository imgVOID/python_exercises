"""
Создайте двухмерный массив размерностью 25 x 25 и умножьте его на единичную матрицу

"""
import numpy


A = numpy.random.randint(1, 25, (25, 25), dtype=numpy.uint8)
B = numpy.eye(25)
C = numpy.dot(A, B)
print(C)

A = numpy.random.randint(1, 4, (4, 4), dtype=numpy.uint8)
B = numpy.eye(4)
C = numpy.dot(A, B)
print(C)
