def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print()
### Распаковка

values_list = [
    1,
    'str',
    [1, 2, 3]
]
values_list2 = [
    'str',
    [1, 2, 3]
]
values_dict = {
    'a': True,
    'b': 2,
    'c': 'string'
}
values_dict2 = {
    'b': 2,
    'c': 'string'
}
print_params(*values_list)
print_params(5, *values_list2)
print_params(**values_dict)
print_params(3, **values_dict2)

