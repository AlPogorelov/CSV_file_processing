from src.csv_aggregate import csv_aggregate


def test_csv_aggregate(test_data):
    assert csv_aggregate(test_data, 'rating=avg') == {'avg': 4.67}
    assert csv_aggregate(test_data, 'rating=min') == {'min': 4.4}
    assert csv_aggregate(test_data, 'rating=max') == {'max': 4.9}

    assert csv_aggregate(test_data, 'rating<max') == {'max': 4.9}
    assert csv_aggregate(test_data, 'rating>min') == {'min': 4.4}
