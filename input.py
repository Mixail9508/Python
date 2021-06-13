import sys


def ddd(rec):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{rec}\n')


if __name__ == '__main__':
    _script_name, price_rec = sys.argv
    ddd(price_rec)
