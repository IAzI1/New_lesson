def main():
    """
    Первое число задает пользователь, пароль должен состоять из
    пары, сумма которых делится на первое число без остатка
    """

    for elem in range(3, 21): # число
        text = f'{elem}: '

        for x in range(1, elem): # первый делитель
            for y in range(x+1, elem): # второй делитель
                if elem % (x+y) == 0:
                    text += f'{x}{y} '


        print(text)



main()