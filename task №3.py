# задание №3
while True:
    input_User = int(input('Введите число: '))
    if input_User == 1:
        print(f'{input_User} процент')
    elif 2 <= input_User <= 4:
        print(f'{input_User} процента')
    elif 5 <= input_User <= 20:
        print(f'{input_User} процентов')
    else:
        print('Введено число больше 20: попробуйте снова')
