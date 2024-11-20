numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primec = []  # список, содержащий только простые числа
not_primec = []  # список, содержащий все не простые числа

for n in numbers:
    if n == 1:
        continue
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            not_primec.append(n)
            break
    else:
        primec.append(n)

print(f'Список простых чисел: {primec}')
print(f'Список непростых чисел: {not_primec}')


# с использованием функции

# def is_prime(numb):
#     if numb < 2:
#         return False
#     for i in range(2, int(numb ** 0.5 + 1)):
#         if numb % i == 0:
#             return False
#     else:
#         return True

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# primec = []  # список, содержащий только простые числа
# not_primec = []  # список, содержащий все не простые числа

# for n in numbers:
#     if is_prime(n):
#         primec.append(n)
#     else:
#         not_primec.append(n)

