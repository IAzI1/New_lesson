# ## Задайте переменные разных типов данных:
# immutable_var = 1, 1.1, 'str', [1, 2, 3]
# print(immutable_var)
#
# ## Изменение значений переменных:
# immutable_var[0] = 10 # Получим TypeError: 'tuple' object does not support item assignment
#
# ## Создание изменяемых структур данных:
# mutable_list = tuple([[1, 2, 3], 4])
# print(f'mutable_list: {mutable_list}')
# mutable_list[0][0] = 4
# mutable_list[0][1] = 5
# mutable_list[0][2] = 6
# print(f'Измененный mutable_list: {mutable_list}')
