def send_email(message, recipient, *, sender="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()
    if '@' not in recipient or '@' not in sender or (
            '.com' not in recipient[-4:] and '.ru' not in recipient[-3:] and '.net' not in recipient[-4:]) or (
            '.com' not in sender[-4:] and '.ru' not in sender[-3:] and '.net' not in sender[-4:]):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Test', 'lena21@gmail.Com')
send_email('Test', 'lena21@mail.ru', sender='lena21@gmail.com')
send_email('Test', 'lena21@mail.ru', sender='lena21@mail.ru')
send_email('Test', 'lena21@mailru', sender='lena21@mail.ru')