# Дан список из предложений-строк.
list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                   "Строковый метод работает быстрее, чем срез",
                   "Для обхода последовательности используйте совместный цикл"]

# Пример генератора кортежа: tuple(item.uppercase() for item in list_of_strings if item)
# 1) Создайте кортеж, содержащий только те предложения, в которых
# встречается словосочетание "тип данных"
result = []
for sequence in list_of_strings:
    if 'тип данных' in sequence:
        result.append(sequence)
result = tuple(result)
print(result)
# Результат: ('Список - изменяемый тип данных', 'Строка - неизменяемый тип данных')


# 2) Создайте кортеж, содержащий только те предложения, которые не начинаются на букву 'с'
result = []
for sequence in list_of_strings:
    if not sequence.lower().startswith('с'):
        result.append(sequence)
result = tuple(result)
print(result)
# Результат: ('Для обхода последовательности используйте совместный цикл',)

