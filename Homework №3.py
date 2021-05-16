import random


def get_jokes():
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    '''
    сделал результат в формате тип лист, на 5 шуток
    '''
    result = []
    for _ in range(5):
        '''
        с помощью метода shuffle перемешал последовательность(изменяя ее внутри функции)
        '''
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        '''
        С помощью метода pop, сделал шутки без повторений 
        '''

        noun = nouns.pop()
        adverb = adverbs.pop()
        adjective = adjectives.pop()
        result_format = f'{noun} {adverb} {adjective}'
        result.append(result_format)
    print(result)


get_jokes()
