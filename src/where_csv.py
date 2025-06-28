from src.strip_arg import strip_arg


def where_csv(dict_f, arg):
    """Функция фильтрует список словарей, по заданому параметру"""
    filtered_dict = []

    col_oper_val = strip_arg(arg)

    column, operator, value = col_oper_val.groups()

    # При фильтрации по не существующей колонке, ответом будет пустой словарь.
    # Для прототипа не проводим валидацию и вызов ошибки

    for row in dict_f:
        for k, v in row.items():
            if k == column:
                if operator == '>':
                    try:    # Перед сравнением < > необходимо чтобы значение было float, иначе нечего сравнивать
                        v = float(v)
                        value = float(value)
                    except ValueError:
                        pass
                    if v > value:
                        filtered_dict.append(row)

                elif operator == '<':
                    try:
                        v = float(v)
                        value = float(value)
                    except ValueError:
                        pass
                    if v < value:
                        filtered_dict.append(row)

                elif operator == '=':
                    if v == value:
                        filtered_dict.append(row)

    return filtered_dict
