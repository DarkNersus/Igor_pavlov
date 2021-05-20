'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
'''

duration = int(input("Введите время в секундах: "))
year = duration // 31556926
month = duration % 31556926 // 2629743
a_week = duration % 31556926 % 2629743 // 604800
day = duration % 31556926 % 2629743 % 604800 // 86400
hours = duration % 31556926 % 2629743 % 604800 % 86400 // 3600
minutes = duration % 31556926 % 2629743 % 604800 % 86400 % 3600 // 60
sec = duration % 31556926 % 2629743 % 604800 % 86400 % 3600 % 60

if duration >= 31556926:
    print(f'год:{year:0} мес:{month:02} нед:{a_week:02} дн:{day:02} час:{hours:02} мин:{minutes:02} сек:{sec:02}')
elif duration >= 2629743:
    print(f'мес:{month:02} нед:{a_week:02} дн:{day:02} час:{hours:02} мин:{minutes:02} сек:{sec:02}')
elif duration >= 604800:
    print(f'нед:{a_week:02} дн:{day:02} час:{hours:02} мин:{minutes:02} сек:{sec:02}')
elif duration >= 86400:
    print(f'дн:{day:02} час:{hours:02} мин:{minutes:02} сек:{sec:02}')
elif duration >= 3600:
    print(f'час:{hours:02} мин:{minutes:02} сек:{sec:02}')
elif duration >= 60:
    print(f'мин:{minutes:02} сек:{sec:02}')
else:
    print(f'сек:{sec:02}')
