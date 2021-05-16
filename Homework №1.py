def num_translate_advcd(drive: str):
    translation_from_english = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль',
    }
    translation = translation_from_english.get(drive.lower())
    if drive.istitle():
        return translation.capitalize()
    return translation


print(num_translate_advcd(input('Enter a numeral from 0 to 10 letters in English: ')))
