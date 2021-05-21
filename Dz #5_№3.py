tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def assigning_classes():
    tutors.append('Катя')
    tutors.append('Николай')
    length_of_the_list_of_tutors = len(tutors)
    length_of_the_class_list = len(klasses)
    for meaning in range(length_of_the_list_of_tutors):
        if length_of_the_class_list > meaning:
            assigning_classes_to_tutors = tutors[meaning] + '', klasses[meaning]
            yield f'{assigning_classes_to_tutors}\n'
        else:
            tutor_without_a_class = tutors[meaning] + '', None
            yield f'{tutor_without_a_class}\n'


generating_work = assigning_classes()

print(next(generating_work), next(generating_work),
      next(generating_work), next(generating_work),
      next(generating_work), next(generating_work),
      next(generating_work), next(generating_work),
      next(generating_work)
      )
# Результат:

# ('Иван', '9А')
#  ('Анастасия', '7В')
#  ('Петр', '9Б')
#  ('Сергей', '9В')
#  ('Дмитрий', '8Б')
#  ('Борис', '10А')
#  ('Елена', '10Б')
#  ('Катя', '9А')
#  ('Николай', None)

print('Генератор истощен', next(generating_work))

# результат работы генератора при вызове функции next(),
# когда в генераторе заканчивается список репетиторов

# ('Иван', '9А')
#  ('Анастасия', '7В')
#  ('Петр', '9Б')
#  ('Сергей', '9В')
#  ('Дмитрий', '8Б')
#  ('Борис', '10А')
#  ('Елена', '10Б')
#  ('Катя', '9А')
#  ('Николай', None)
#     print('Генератор истощен', next(generating_work))
# StopIteration
