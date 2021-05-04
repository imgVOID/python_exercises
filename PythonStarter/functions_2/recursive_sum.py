# Напишите рекурсивную функцию, вычисляющую сумму натуральных чисел из заданного промежутка.

def recur_sum(limit):
    global START
    if limit == START:
        return START
    else:
        return limit + recur_sum(limit - 1)


START = int(input("Enter a positive number"))
END = int(input("Enter a positive number"))
while True:
    if START < 1:
        START = int(input("Enter a positive number"))
    elif END < 1:
        END = int(input("Enter a positive number"))
    else:
        break

print("The sum is", recur_sum(END))
