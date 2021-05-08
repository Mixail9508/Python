# задание номер №2

result = []
sum_number = 0

for number in range(1, 1000, 2):
    result.append(number ** 3)
for number in result:
    sum_numb = 0
    number_copy = number
    while number_copy > 0:
        numbers = number_copy % 10
        sum_numb += numbers
        number_copy //= 10
    if sum_numb % 7 == 0:
        sum_number += number
print(sum_number)

sum_number = 0
for number in result:
    sum_numb = 0
    number_copy = number + 17
    while number_copy > 0:
        numbers = number_copy % 10
        sum_numb += numbers
        number_copy //= 10
    if sum_numb % 7 == 0:
        sum_number += (number + 17)
print(sum_number)