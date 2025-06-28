import pytest

from tabulate import tabulate
from src.tabulete import print_tabl


def test_tabulate_print_list_dict(test_data_print, capsys):

    expected_tabulate = tabulate(
        [
            ['iphone 15 pro', 'apple'], ['galaxy s23 ultra', 'samsung']
        ],
        headers=['name', 'brand'],
        tablefmt='grid'
    )
    print_tabl(test_data_print)

    captured = capsys.readouterr()

    assert captured.out.strip() == expected_tabulate.strip()


def test_tabulate_print_dict(test_print_one_dict, capsys):
    expected_tabulate = tabulate(
        [['199']],
        headers=['min'],
        tablefmt='grid'
    )
    print_tabl(test_print_one_dict)

    captured = capsys.readouterr()

    assert captured.out.strip() == expected_tabulate.strip()

