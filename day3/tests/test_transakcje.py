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
