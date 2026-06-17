from functools import reduce

transactions = [
    {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},
    {'id': 2, "type": "expense", "amount": 200, "currency": "USD"},
    {'id': 3, "type": "income", "amount": 500, "currency": "USD"},
    {'id': 4, "type": "expense", "amount": 300, "currency": "USD"},
    {'id': 5, "type": "income", "amount": 700, "currency": "USD"},
    {'id': 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
]


# filtrowac transakcje - -> list
# mapowac transakcje -> currency, ma wstawic 0
# potem zsumowac te transakcje - reduce

# raport - łacząca te operacje

def filter_transactions(transactions, transaction_type):
    """
    Filtruje transakcje p otypie transakcji: income, expense
    :param transactions:
    :param transaction_type:
    :return: lista transakcji
    """
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    """
    Mapuje transakcje spełniające warunek waluty
    :param transactions:
    :param currency:
    :return: lista transakcji
    """
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(mapped):
    """
    Zsumuje kwoty transakcji
    :param mapped:
    :return: suma transakcji int, float
    """
    return reduce(lambda x, y: x + y, mapped, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total


def test_transactions_processing():
    assert (map_transactions(filter_transactions(transactions, "income"), "USD")
            == [1000, 500, 700, 0])


if __name__ == '__main__':
    print(process_transactions(transactions, "expense", "EUR"))
# 400

# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day3> pytest -v .\transakcje.py
# ============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.14.6, pytest-9.1.0, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day3
# collected 1 item
#
# transakcje.py::test_transactions_processing PASSED                                                                                                                          [100%]
#
# =============================================================================== 1 passed in 0.01s ================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day3>
