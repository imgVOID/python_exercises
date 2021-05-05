# Даны два списка. Создайте из них словарь:
# 1) Используя функцию zip()
# 2) Используя генератор словаря
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# 1)
dict_1 = dict(zip(keys, values))

# 2)
dict_2 = {key.upper(): value*20 for key in keys for value in values}

print(dict_1, dict_2, sep='\n')
# Вывод:
# {'Ten': 30, 'Twenty': 30, 'Thirty': 30}
s = {key: value for key in keys for value in values}

