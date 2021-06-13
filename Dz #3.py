import sys

import itertools


def destination_function(hobby_f, users_f, distribution):
    with open(hobby_f, 'r', encoding='utf-8') as hobby, \
            open(users_f, 'r', encoding='utf-8') as users, \
            open(distribution, 'a', encoding='utf-8') as distribution:
        for human, hobbies in itertools.zip_longest(users, hobby):

            # если хобби будет больше чем пользователей будет ошибка и записи в файл не будет.

            if human is None:
                exit(1)
            else:

                # если пользователей будет больше чем их хобби запишется users: None.

                human = human.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                distribution.write(f'{human}: {hobbies}\n')


if __name__ == '__main__':
    _script_name, hobby_f, users_f, distribution = sys.argv
    print(destination_function('hobby.csv', 'users.csv', 'distribution.csv'))
