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
