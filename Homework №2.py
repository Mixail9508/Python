def thesaurus_advcd(*full_name_list: str):
    result = {}
    for full_name in full_name_list:
        name, surname = full_name.split()
        surname_result = result.setdefault(surname[0], {})
        name_result = surname_result.setdefault(name[0], [])
        name_result.append(full_name)
    return result


print(
    thesaurus_advcd(
        "Иван Сергеев", "Инна Серова",
        "Петр Алексеев", "Илья Иванов", "Анна Савельева"
    )
)
