# задание №4
prfessiya_and_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                      'директор аэлита']

for hi_name in prfessiya_and_name:
    result = hi_name.split()[-1]

    print(f"'Привет, {result.capitalize()}!'")
