import unittest


def divide(a, b):
    return a / b


# PascalCase
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


class MyTestCase(unittest.TestCase):
    def test_somthing(self):
        self.assertEqual(True, False)
# Expected :True
# Actual   :False

if __name__ == '__main__':
    unittest.main()
