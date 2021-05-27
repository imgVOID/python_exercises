"""
Создайте метакласс, записывающий в файл всю информацию о классах, которые используют его в качестве метакласса.
Используйте def __new__(mcs, name, bases, attrs) где name - это имя класса, msc - метакласс;
в методе __new__ используйте return super().__new__(mcs, name, bases, attrs)

"""


class Meta(type):
    pass


class A(metaclass=Meta):
    pass


class B(metaclass=Meta):
    pass


class C(metaclass=Meta):
    pass


class D:
    pass



