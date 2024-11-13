def check_type():
    numb = input('Введите число: ')
    if numb.isdigit():
        return int(numb)
    print('Ошибка типа данных! Введите целое число. Попробуй еще раз!')
    return check_type()


first = check_type()
second = check_type()
third = check_type()

if first == second and second == third:  # проверяем что все числа равны
    print(3)
elif first == second or first == third or second == third:  # ищем 2 одинаковых числа
    print(2)
else:
    print(0)
