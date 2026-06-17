# assert - asercja - test

x = 5
assert x == 5

# assert x == 15
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day3\tests\test_transakcje.py", line 5, in <module>
#     assert x == 15
#            ^^^^^^^
# AssertionError

# map, reduce, filter
import transakcje as tr  # jako alias


def test_maap_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert tr.map_transactions(tr.transactions, "USD") == result


def test_reduce_transactions():
    assert tr.reduce_transactions([1000, 500, 700, 0]) == 2200


# day3/tests/test_transakcje.py::test_maap_transactions_usd PASSED         [ 50%]
# day3/tests/test_transakcje.py::test_reduce_transactions PASSED           [100%]

def test_filter_transactions_income():
    expected_list = [
        {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},

        {'id': 3, "type": "income", "amount": 500, "currency": "USD"},

        {'id': 5, "type": "income", "amount": 700, "currency": "USD"},

        {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

    assert tr.filter_transactions(tr.transactions, "income") == expected_list


# day3/tests/test_transakcje.py::test_maap_transactions_usd PASSED         [ 33%]
# day3/tests/test_transakcje.py::test_reduce_transactions PASSED           [ 66%]
# day3/tests/test_transakcje.py::test_filter_transactions_income PASSED    [100%]


# testy parametryzowane
import pytest


@pytest.mark.parametrize(
    "kind,currency,expected",
    [
        ("income", "USD", 1000 + 500 + 700),
        ("income", "EUR", 100),
        ("expense", "USD", 200 + 300),
        ("expense", 'EUR', 400)
    ]
)
def test_process_transactions_param(kind, currency, expected):
    assert tr.process_transactions(tr.transactions, kind, currency) == expected
# day3/tests/test_transakcje.py::test_maap_transactions_usd PASSED         [ 14%]
# day3/tests/test_transakcje.py::test_reduce_transactions PASSED           [ 28%]
# day3/tests/test_transakcje.py::test_filter_transactions_income PASSED    [ 42%]
# day3/tests/test_transakcje.py::test_process_transactions_param[income-USD-2200] PASSED [ 57%]
# day3/tests/test_transakcje.py::test_process_transactions_param[income-EUR-100] PASSED [ 71%]
# day3/tests/test_transakcje.py::test_process_transactions_param[expense-USD-500] PASSED [ 85%]
# day3/tests/test_transakcje.py::test_process_transactions_param[expense-EUR-400] PASSED [100%]
