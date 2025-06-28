from src.strip_arg import strip_arg


def csv_aggregate(dict_, arg):
    '''Проводит аггригацию таблицы по min max avg'''

    col_oper_val = strip_arg(arg)

    column, pass_, operation = col_oper_val.groups()

    result = []

    # Не учтено что может передаваться другой логический оператор кроме "=",
    # но для прототипа условно считаем что всегда передается "="

    for row in dict_:
        if column in row:
            result.append(float(row[column]))

    if operation == 'avg':
        result = {'avg': str(round((sum(result) / len(result)), 2))}

    elif operation == 'max':
        result = {'max': str(max(result))}

    elif operation == 'min':
        result = {'min': str(min(result))}

    # result = dict(result)

    return result
