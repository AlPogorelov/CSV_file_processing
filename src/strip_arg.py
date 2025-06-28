import re


def strip_arg(arg):
    '''Преобразуем строку переданного аргумента в список для дальнейшего использования '''

    col_oper_val = re.match(r'([^<>=!]+)([<>=!]+)(.+)', arg.strip())

    return col_oper_val
