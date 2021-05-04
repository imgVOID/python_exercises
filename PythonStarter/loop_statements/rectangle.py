# Выведите на экран прямоугольник заданных высоты и ширины:
x = int(input("Введите ширину:"))
y = int(input("Введите длину:"))
# Вариант с одним циклом:
for i in range(y):
    print('*' * x)

# Вариант с двумя циклами:
for i in range(y):
    for j in range(x):
        print('*', end="")
    print()
