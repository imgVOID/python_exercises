"""
Создайте программу, сохраняющую в .txt-файл список из тысячи простых чисел.
Для этого импортируйте из пакета primes все необходимые функции
и определите функцию print_primes(), которая при передаче имени файла
записывает простые числа в него, в другом случае - выводит на экран.
Рассмотрите код импортированных модулей и создайте необходимый
генератор списка для получения списка простых чисел.

"""


def print_primes(filename=None, number_of_primes=1):
    if type(filename) is str and '.txt' in filename:
        pass
    else:
        pass


if __name__ == '__main__':
    print_primes('text.txt', 1000)
