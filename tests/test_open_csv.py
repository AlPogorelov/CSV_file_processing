from src.open_csv import open_csv


def test_open_csv():

    dir_test_csv = 'tests/tests_csv.csv'

    assert open_csv(dir_test_csv) == [{'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'}]
