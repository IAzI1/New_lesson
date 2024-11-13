
###  Работа со словарями:

my_dict = {'Kate': '10.02.1994',
           'Jade': '01.04.1999'}
print(f'Dict: {my_dict}')

print(f"Existing value: {my_dict['Kate']}")
print(f"Not existing value: {my_dict.get('Tomas', 'Нет данных')}")

# user_key = input('Введите ключ: ').title()
#
# if my_dict.get(user_key):
#     print(f'Ключ {user_key}: {my_dict[user_key]}')
# else:
#     print(f'Нет данных по ключу {user_key}')

my_dict.update({'Max': '03.03.2002',
                'Tom': '21.09.1997'})

print(f'Add data: {my_dict}')

del_key = 'Kate'
print(f'Удален ключ "{del_key}" со значением: {my_dict.pop(del_key)}')
print(f'Modified dictionary: {my_dict}')

print('-' * 100)
### Работа с множествами:

my_set = {1, 2, 3, '1', '2', (2, 3), True, 2, 3, True}

print(f'Set: {my_set}')

# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет
my_set.add(5)
my_set.add(0.1)

# Удалите один любой элемент из множества my_set
my_set.discard(True)

print(f'Modified set: {my_set}')
