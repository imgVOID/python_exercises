"""
Создайте метакласс, записывающий в файл всю информацию о классах, которые используют его в качестве метакласса.
Используйте def __new__(mcs, name, bases, attrs) где name - это имя класса, msc - метакласс;
в методе __new__ используйте return super().__new__(mcs, name, bases, attrs)

"""
def hello():
    print('hello!!!')

class Meta(type):
    attribute = 2

    def __new__(mcs, name, bases, attrs):
        with open('practical.txt', 'a') as f:
            result = f'{name}\n{bases}\n{attrs}\n\n'
            f.write(result)
            attrs['hello'] = hello
            new_class = super().__new__(mcs, name, bases, attrs)
        return new_class


class A(metaclass=Meta):
    pass


class B(metaclass=Meta):
    pass


class C(metaclass=Meta):
    pass


class D:
    pass


print(A.attribute)
print(A.hello())
print(A.__bases__)
print(type(A))
