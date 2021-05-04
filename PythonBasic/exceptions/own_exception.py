"""
Опишите свой класс исключения.
Напишите функцию, которая будет выбрасывать данное исключение,
если пользователь введёт определённое значение,
и перехватите это исключение при вызове функции.
"""


class ValueNotInRange(Exception):
    def __init__(self, number, minimum, maximum):
        message = f'number isn\'t between {minimum} to {maximum}: {number}'
        super().__init__(message)


def input_check(minimum, maximum):
    number = int(input(f"Enter a number between {minimum} to {maximum}:"))
    if not minimum <= number <= maximum:
        raise ValueNotInRange(number, minimum, maximum)
    print(f'Value {number} is correct!')
    return number


def main():
    while True:
        try:
            value = input_check(0, 10)
        except ValueError as e:
            # Доступ к сообщению ошибки можно получить через
            # обращение к первому её аргументу:
            print(e.args[0], end='\n\n')
        except ValueNotInRange as e:
            # Внутри функции print() ошибка будет представлена её сообщением:
            print(e, end='\n\n')
        else:
            if value is not None:
                break


if __name__ == '__main__':
    main()
