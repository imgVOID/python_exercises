"""
Напишите программу, которая открывает текстовый файл и выводит на экран
каждую строчку текста по очереди, подписывая её порядковым номером.
Затем выведите на экран количество линий в тексте.

"""

# Для открытия файла используйте конструкцию with open(path, 'r') as f:
# Для получения списка с линиями текста используйте метод file.readlines()
# Функция enumerate(list) возвращает список из кортежей с парами индекс-значение


def file_lengthy(path):
    with open(path, 'r') as f:
        return None


print("Number of lines in the file:", file_lengthy("data/file.txt"), end='\n\n')
