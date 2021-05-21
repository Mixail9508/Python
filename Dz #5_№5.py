src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# убираем повторяющиеся элементы в корзину, оставляя только уникальные числа

unique_numbers = set()
basket = set()
for number in src:
    if number not in basket:
        unique_numbers.add(number)
    else:
        unique_numbers.discard(number)
    basket.add(number)

print(unique_numbers)

# {1, 3, 4, 10, 11, 23} - ответ

# приводим полученые унмкальные номера к исходному порядку в списке

src_old = [number for number in src if number in unique_numbers]
print(src_old)

# [23, 1, 3, 10, 4, 11] - ответ
