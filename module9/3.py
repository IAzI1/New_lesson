first = ['Strings', 'Student', 'Computers']

second = ['Строка', 'Урбан', 'Компьютер']

def is_len(a, b):
    return len(a) == len(b)

first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
second_result = (map(is_len, first, second))

print(type(first_result))
print(list(first_result))
print(list(second_result))