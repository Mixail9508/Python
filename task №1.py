# задание номер №1
# до минуты
duration = 25
if duration <= 60:
    print(f'{duration} секунд(ы)')
else:
    print("неверное число в минуте 60 секунд")

# до часа
duration = 2555
secund = duration
minut = secund // 60

print(f'{minut} мин. {secund % 60} сек.')

# до суток
duration = 64896
secund = duration
minut = secund // 60
hour = minut // 60
print(f'{hour} час. {minut % 60} мин. {secund % 60} сек.')

# до месяца
duration = 2556995
secund = duration
minut = secund // 60
hour = minut // 60
day = hour // 24
print(f'{day} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')

# до года

duration = 119569266
secund = duration
minut = secund // 60
hour = minut // 60
day = hour // 24
month = day // 30

print(f'{month} мес. {day % 30} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')

# больше года
duration = 1009821632
secund = duration
minut = secund // 60
hour = minut // 60
day = hour // 24
month = day // 30
year = month // 12

print(f'{year} гд. {month % 12} мес. {day % 30} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')

# общее преобразование на секунды, часы, дни, месяцы, года, и более
while True:
    duration = int(input('Введите секунды: '))

    secund = duration
    minut = secund // 60
    hour = minut // 60
    day = hour // 24
    month = day // 30
    year = month // 12

    if secund < 60:
        print(f'{secund} сек.')
    elif minut < 60:
        print(f'{minut} мин. {secund % 60} сек.')
    elif hour < 24:
        print(f'{hour} час. {minut % 60} мин. {secund % 60} сек.')
    elif day < 30:
        print(f'{day} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')
    elif month < 12:
        print(f'{month} мес. {day % 30} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')
    else:
        print(f'{year} гд. {month % 12} мес. {day % 30} дн. {hour % 24} час. {minut % 60} мин. {secund % 60} сек.')
