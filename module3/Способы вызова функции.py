def check_char(wrds, char_list):
    """
    :param wrds: str
    :param char_list: list str которые нужно проверить
    :return: False если хотяб в одном слове отсутствует строка из списка char_list
    """
    for wrd in wrds:
        for char in char_list:
            if not wrd.endswith(char):
                return False

    return True



def send_email(message, addressee, sender='university.help@gmail.com'):
    char_list = [".com", ".ru", ".net"]

    # если отправитель и получатель один и тот же адрес
    if addressee == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    # Если нет знака @ в почте
    if '@' not in addressee or '@' not in sender:
        print('Отсутствует знак @ в почтах')
        return

    # Если же addressee и sender совпадают, то вывести невозможно отправить письмо
    if check_char([addressee, sender], char_list):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{addressee}>')
        return

    # Если отправитель по умолчанию
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{addressee}>')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{addressee}>')



send_email('university.help@gmail.com', "university.helpg@mail.com")
send_email('university.help@gmail.com', "university.help@gmail.com")
send_email('university.help@gmail.com', "university.helpgmail.com")
send_email('university.help@gmail.com', "university.helpg@mail")
send_email('university.help@gmail.com', "university.helpg@mail.com", sender='iin@mail.ru')