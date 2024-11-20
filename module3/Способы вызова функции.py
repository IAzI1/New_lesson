def send_email(message, recipient, sender='university.help@gmail.com'):
    char_list = ".com", ".ru", ".net"

    # если отправитель и получатель один и тот же адрес
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    # Если нет знака @ в почте
    elif '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        return

    # Если же addressee и sender совпадают, то вывести невозможно отправить письмо
    elif not recipient.endswith(char_list) or not sender.endswith(char_list):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        return

    else:
        print(f'Ваше сообщение: {message}')
        # Если отправитель по умолчанию
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')


# Тестовые данные
send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
print()
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
print()
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
print()
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
