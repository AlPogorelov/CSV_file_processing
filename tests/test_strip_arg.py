from src.strip_arg import strip_arg


def test_strip_arg():

    assert strip_arg('brand=apple').groups() == ('brand', '=', 'apple')
    assert strip_arg('price>100').groups() == ('price', '>', '100')
