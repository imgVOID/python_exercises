"""
Создайте матрицу размерностью 12 x 12, транспонируйте её,
возведите каждый элемент матрицы в квадрат и умножьте на 2.
Вычтите из данной матрицы единичную матрицу
и распечатайте результат на консоль.

"""
import numpy

print('Матрица 12х12:')
A = numpy.random.randint(1, 10, (12, 12), dtype=numpy.uint8)
print(A)
print('Транспонированная матрица:')
print(A.T)
print('Транспонированная матрица, значения которой возведены в квадрат:')
print(A.T ** 2)
print('Транспонированная матрица, значения которой возведены в квадрат и умножены на 2:')
print(A.T ** 2 * 2)