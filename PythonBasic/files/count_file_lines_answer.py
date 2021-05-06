"""
Напишите программу, которая открывает текстовый файл и выводит на экран
каждую строчку текста по очереди, подписывая её порядковым номером.
Затем выведите на экран количество линий в тексте.

"""


def file_lengthy(path):
    """Функция со счетчиком"""
    print('1)', file_lengthy.__doc__, end=':\n\n')
    with open(path, 'r') as f:
        count = 0
        for line in f.readlines():
            count += 1
            print(f'{count} line:\n{line}', end='')
        return count


print("\nNumber of lines in the file:", file_lengthy("data/file.txt"), end='\n\n')


def file_lengthy(path):
    """Функция с использованием enumerate(list)"""
    print('2)', file_lengthy.__doc__, end=':\n\n')
    with open(path, 'r') as f:
        for index, line in enumerate(f.readlines()):
            print(f'{index + 1} line:\n{line}', end='')
        return index + 1


print("\nNumber of lines in the file:", file_lengthy("data/file.txt"), end='\n\n')