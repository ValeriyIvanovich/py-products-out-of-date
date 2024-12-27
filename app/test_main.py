import datetime

import pytest

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, expected",
    [
        (datetime.date(2022, 2, 5), []),
        (datetime.date(2022, 2, 10), ["chicken"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken"]),
        (datetime.date(2022, 2, 12), ["salmon", "chicken", "duck"]),
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mocked_date: mock.MagicMock, today_date: datetime.date, expected: list
) -> None:

    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 11),
            "price": 160
        },
    ]
    mocked_date.date.today.return_value = today_date
    result = outdated_products(product_list)
    assert result == expected
