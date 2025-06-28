from src.where_csv import where_csv


def test_where_csv(test_data):
    result = where_csv(test_data, 'brand=apple')
    assert result[0]['name'] == 'iphone 15 pro'
    assert result[0]['price'] == '999'
    assert len(result) == 1

    result = where_csv(test_data, 'price>1000')
    assert result[0]['name'] == 'galaxy s23 ultra'
    assert result[0]['price'] == '1199'
    assert len(result) == 1

    result = where_csv(test_data, 'price<1000')
    assert result[0]['name'] == 'iphone 15 pro'
    assert result[0]['price'] == '999'
    assert len(result) == 3
