# задание №3
# из темы передача функции параметров в другую функцию лямда - функция, и функции map

text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0

for _ in range(len(text)):
    text_elements = text[index]

    sign = ''
    if text_elements.startswith(('+', '-')):
        sign, text_elements = text_elements[0], text_elements[1:]

    if text_elements.isdigit():
        number = int(text_elements)

        # преобразуем число
        text[index] = f'{sign}{number:02d}'
        # заключаем кавычками число в списке
        text.insert(index, '"')
        text.insert(index + 2, '"')

        # нужно прибавить к индексу 3, потому что добавили 2 элемента(кавычки)
        index += 3
    else:
        index += 1

text_as_string = " ".join(text)

# кавычки парные, поэтому используем четное и нечетное интерации, чтобы
# грамотно отформотировать
for iteration_number in range(text_as_string.count(' " ')):
    # если интерация четная
    if iteration_number % 2:
        text_as_string = text_as_string.replace(' " ', '" ',1)
    else:
        text_as_string = text_as_string.replace(' " ', ' "', 1)

print(text_as_string)