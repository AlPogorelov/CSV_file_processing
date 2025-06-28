from tabulate import tabulate


def print_tabl(dict_):
    """Принтуем результат в таблицу"""

    if isinstance(dict_, list) and dict_ and isinstance(dict_[0], dict):  # Если список словарей

        headers = dict_[0].keys()
        rows = [item.values() for item in dict_]
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    elif isinstance(dict_, dict):  # Если один словарь

        headers = dict_.keys()
        value = dict_.values()

        print(tabulate([value], headers=headers, tablefmt="grid"))
