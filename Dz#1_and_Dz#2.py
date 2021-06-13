from collections import Counter

import requests

# генератор перебирает из записанного файла нужные нам данные


IP_INDEX = 0
METHOD_INDEX = 5
URL_INDEX = 6


def format_generator():
    # берем данные с сайта и записываем в файл.

    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    response = requests.get(url).text
    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        f.write(response)

    # полученные данные перебираем и выводим то, что нам было нужно.

    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split()
            remote_addr = line[IP_INDEX]
            request_type = line[METHOD_INDEX].strip('" ')
            requested_resource = line[URL_INDEX]
            yield remote_addr, request_type, requested_resource


# Находим спамера и выводим количество его запросов.

def spammer():
    ip_counter = Counter(spam_IP[IP_INDEX] for spam_IP in format_generator())
    yield print(ip_counter.most_common(1))


if __name__ == '__main__':
    print(next(format_generator()))
    print(*spammer())
