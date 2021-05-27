"""
Даны классы Directory и File.
Создайте тесты для методов Directory.add_file(),
Directory.remove_file(), а также File.__init__()

"""

import typing
import unittest


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


class DirectoryTestCase(unittest.TestCase):
    def test_directory_initialisation(self):
        name = '1'
        files = [File(name='1.1.'), File(name='1.2.')]
        directory = Directory(name='1', files=files)

        self.assertIs(directory.name, name)
        self.assertListEqual(directory.files, files)
        self.assertListEqual(directory.sub_directories, [])
        self.assertIs(files[0].directory, directory)
        self.assertIs(files[1].directory, directory)

    def test_add_sub_directory(self):
        root = Directory(name='1', files=[File(name='1.1.')])
        sub_directory = Directory(name='10', files=[File(name='10.1.')])
        root.add_sub_directory(sub_directory)

        self.assertIn(sub_directory, root.sub_directories)
        self.assertIs(sub_directory.root, root)

    def test_remove_sub_directory(self):
        root = Directory(name='1', files=[File(name='1.1.')])
        sub_directory_1 = Directory(name='10', files=[File(name='10.1.')])
        sub_directory_2 = Directory(name='20', files=[File(name='20.1.')])
        root.add_sub_directory(sub_directory_1)
        root.add_sub_directory(sub_directory_2)
        root.remove_sub_directory(sub_directory_1)

        self.assertNotIn(sub_directory_1, root.sub_directories)
        self.assertIn(sub_directory_2, root.sub_directories)
        self.assertIsNone(sub_directory_1.root)
        self.assertIs(sub_directory_2.root, root)

    def test_add_file(self):
        file = File(name='1.1.')
        directory = Directory(name='1', files=[file])

        self.assertIn(file, directory.files)
        self.assertIs(file.directory, directory)

    def test_remove_file(self):
        file_1 = File('1.1.')
        file_2 = File('1.2.')
        directory = Directory(name='1', files=[file_1, file_2])
        directory.remove_file(file_1)

        self.assertNotIn(file_1, directory.files)
        self.assertIn(file_2, directory.files)
        self.assertIsNone(file_1.directory)
        self.assertIs(file_2.directory, directory)


class FileTestCase(unittest.TestCase):
    def test_file_initialisation(self):
        name = '1.1.'
        file = File(name=name)

        self.assertIs(file.name, name)
        self.assertIsNone(file.directory)
