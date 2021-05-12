# задание №5
price_list = [36.63, 60.51, 80.45, 85.56, 68.54, 89.6, 23.77, 37.41, 36.3, 81.99, 92.65, 80.0, 43.8, 79.12, 54.41]

the_right_price = []
for price in price_list:
    price_as_str = str(price)
    price_as_list = price_as_str.split('.')

    if len(price_as_list) == 1:
        rubles, kopeykas = *price_as_list, 0
    elif len(price_as_list) == 2:
        rubles, kopeykas = price_as_list
    else:
        continue
    int_rubles, int_kopekyas = int(rubles), int(kopeykas)
    formatted_price = f'{int_rubles} руб. {int_kopekyas:02d} коп'
    the_right_price.append(formatted_price)

print('.  '.join(the_right_price))
print(id(the_right_price))  # id до
# сортируем по возрастанию без созднаия нового списка
the_right_price.sort()

print(*the_right_price)
print(id(the_right_price))  # id после, одинаковые с id до

# создать новый список в порядке убывания
new_price_list = list(reversed(the_right_price))

print(*new_price_list)
print(id(new_price_list))  # новый id списка

print(*new_price_list[:5])  # 5 самых дорогих товаров
