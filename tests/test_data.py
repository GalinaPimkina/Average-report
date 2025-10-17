import pytest

from utils.parser import get_one_type
from utils.rating import get_data_for_rating, average_rating, get_items_for_rating
from utils.products import get_products_data


@pytest.mark.parametrize(
    ('string', 'expected'),
    [
        ('average-rating', 'average_rating'),
        ('one-two', 'one_two'),
    ]
)
def test_get_one_type(string: str, expected: str):
    assert get_one_type(string) == expected


@pytest.mark.parametrize(
    ('data', 'report_type', 'expected'),
    [
        (
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2},
                'poco x5 pro': {'brand': 'xiaomi', 'price': 299, 'rating': 4.4},
                'iphone se': {'brand': 'apple', 'price': 429, 'rating': 4.1},
                'galaxy z flip 5': {'brand': 'samsung', 'price': 999, 'rating': 4.6},
                'redmi 10c': {'brand': 'xiaomi', 'price': 149, 'rating': 4.1},
                'iphone 13 mini': {'brand': 'apple', 'price': 599, 'rating': 4.5}
            },
            'average_rating',
            {
                'apple': [4.9, 4.7, 4.1, 4.5],
                'samsung': [4.8, 4.2, 4.6],
                'xiaomi': [4.6, 4.4, 4.1]
            }
        ),
        (
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2}
            },
            'average_rating',
            {
                'apple': [4.9, 4.7],
                'samsung': [4.8, 4.2],
                'xiaomi': [4.6]
            }

        )
    ]
)
def test_get_data_for_rating(data: dict, report_type: str, expected: dict):
    assert get_data_for_rating(data, report_type) == expected


@pytest.mark.parametrize(
    ('data', 'report_type', 'expected'),
    [
        (
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2},
                'poco x5 pro': {'brand': 'xiaomi', 'price': 299, 'rating': 4.4},
                'iphone se': {'brand': 'apple', 'price': 429, 'rating': 4.1},
                'galaxy z flip 5': {'brand': 'samsung', 'price': 999, 'rating': 4.6},
                'redmi 10c': {'brand': 'xiaomi', 'price': 149, 'rating': 4.1},
                'iphone 13 mini': {'brand': 'apple', 'price': 599, 'rating': 4.5}
            },
            'average_rating',
            {
                'apple': 4.55,
                'samsung': 4.53,
                'xiaomi': 4.37
            }
        ),
        (
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2}
            },
            'average_rating',
            {
                'apple': 4.8,
                'xiaomi': 4.6,
                'samsung': 4.5
            }
        )
    ]
)
def test_average_rating(data: dict, report_type: str, expected: dict):
    assert average_rating(data, report_type) == expected


@pytest.mark.parametrize(
    ('report_type', 'expected'),
    [
        ('average_rating', ('brand', 'rating')),
        ('average_price', ('brand', 'price')),
    ]
)
def test_get_items_for_rating(report_type, expected):
    assert get_items_for_rating(report_type) == expected


@pytest.mark.parametrize(
    ('files', 'expected'),
    [
        (
            ['files/products/products1.csv', 'files/products/products2.csv'],
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                 'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                 'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                 'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                 'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2},
                 'poco x5 pro': {'brand': 'xiaomi', 'price': 299, 'rating': 4.4},
                 'iphone se': {'brand': 'apple', 'price': 429, 'rating': 4.1},
                 'galaxy z flip 5': {'brand': 'samsung', 'price': 999, 'rating': 4.6},
                 'redmi 10c': {'brand': 'xiaomi', 'price': 149, 'rating': 4.1},
                 'iphone 13 mini': {'brand': 'apple', 'price': 599, 'rating': 4.5}
             },
        ),
        (
            ['files/products/products1.csv'],
            {
                'iphone 15 pro': {'brand': 'apple', 'price': 999, 'rating': 4.9},
                'galaxy s23 ultra': {'brand': 'samsung', 'price': 1199, 'rating': 4.8},
                'redmi note 12': {'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
                'iphone 14': {'brand': 'apple', 'price': 799, 'rating': 4.7},
                'galaxy a54': {'brand': 'samsung', 'price': 349, 'rating': 4.2}
            },
        )
    ]
)
def test_get_products_data(files: list, expected: dict):
    assert get_products_data(files) == expected