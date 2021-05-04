# Дан список из предложений-строк
list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                   "Строковый метод работает быстрее, чем срез",
                   "Для обхода последовательности используйте совместный цикл"]

# С помощью генератора списков создайте кортеж, содержащий только слова, начинающиеся на букву "с".
result = tuple(word.lower() for sentence in list_of_strings
               for word in sentence.split(' ')
               if word.lower().startswith('с'))
print(result)
# Результат: ('список', 'строка', 'строковый', 'срез', 'совместный')
