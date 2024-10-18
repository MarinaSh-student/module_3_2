def send_email (message, recipient, *, sender = 'university.help@gmail.com'):
    a = '@'
    while 1 > 0:
        if a not in recipient and sender:
            if (".com" or ".ru" or ".net") not in (recipient or sender):
                print('Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru')
                break
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            break
        if sender == 'university.help@gmail.com':
            print("Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com")
            break
        elif sender != 'university.help@gmail.com':
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru')
            break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение, как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.studentmail.uk', sender='urban.teachermail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
