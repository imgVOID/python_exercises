"""
Дополнительное задание.
Расширьте функционал класса Directory двумя методами:
1. Добавление файла в директорию
(add_file, принимает экземпляр File и присваивает ему поле directory);
2. Удаление файла из директории
(remove_file, принимает экземпляр File и обнуляет у него поле directory.
Также метод удаляет файл из списка files).
Реализуйте у класса File поле directory типа Directory.
Реализуйте строковое представление классов Directory и File.

"""

import typing


class Directory:
    def __init__(self, name: str, files: typing.List['File']) -> None:
        self.name: str = name
        self.root: typing.Union[Directory, None] = None
        self.files: typing.List[File] = []
        for file in files:
            file.directory = self
            self.files.append(file)
        self.sub_directories: typing.List[Directory] = []

    def __repr__(self) -> str:
        return f'Directory("{self.name}")'

    def add_sub_directory(self, directory: 'Directory') -> None:
        directory.root = self
        self.sub_directories.append(directory)

    def remove_sub_directory(self, directory: 'Directory') -> None:
        directory.root = None
        self.sub_directories.remove(directory)

    def add_file(self, file: 'File') -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: 'File') -> None:
        file.directory = None
        self.files.remove(file)


class File:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.directory: typing.Union[Directory, None] = None

    def __repr__(self) -> str:
        return f'File({self.name})'


if __name__ == '__main__':
    ten = Directory('10', [File('10.1.')])
    twenty = Directory('20', [File('20.1.')])
    one = Directory('1', [File('1.1.')])
    one.add_sub_directory(ten)
    one.add_sub_directory(twenty)
    print(f'ten.root = {ten.root},',
          f'twenty.root = {twenty.root},',
          f'one.sub_directories = {one.sub_directories}')
    one.remove_sub_directory(ten)
    print(f'ten.root = {ten.root},',
          f'twenty.root = {twenty.root},',
          f'one.sub_directories = {one.sub_directories}')
    file = File('1.2.')
    one.add_file(file)
    print(f'one.files = {one.files},',
          f'file.directory = {file.directory}')
    one.remove_file(file)
    print(f'one.files = {one.files},',
          f'file.directory = {file.directory}')
    # one.add_file('hello')
