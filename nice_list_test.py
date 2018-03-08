import unittest

from nice_list import nice_format


class NiceListFormattingTest(unittest.TestCase):
    def test_format_single_str(self):
        self.assertEqual('John', nice_format(('John',)))

    def test_format_two_str(self):
        self.assertEqual('Bob and Alice', nice_format(('Bob', 'Alice')))

    def test_format_many_str(self):
        self.assertEqual('Bob, Alice, Charles, Donald and Eric',
                         nice_format(('Bob', 'Alice', 'Charles', 'Donald', 'Eric')))

    def test_format_single_str_quote(self):
        self.assertEqual('"John"', nice_format(('John',), string_quotes='"'))

    def test_format_two_str_quote(self):
        self.assertEqual('"Bob" and "Alice"', nice_format(('Bob', 'Alice'), string_quotes='"'))

    def test_format_many_str_quote(self):
        self.assertEqual('"Bob", "Alice", "Charles", "Donald" and "Eric"',
                         nice_format(('Bob', 'Alice', 'Charles', 'Donald', 'Eric'), string_quotes='"'))

    def test_format_single_int(self):
        self.assertEqual('1', nice_format((1,)))

    def test_format_two_int(self):
        self.assertEqual('1 and 2', nice_format((1, 2)))

    def test_format_many_int(self):
        self.assertEqual('1, 2, 3, 4 and 5', nice_format((1, 2, 3, 4, 5)))

    def test_format_single_str_no_and(self):
        self.assertEqual('1', nice_format((1,), use_and=False))

    def test_format_two_str_no_and(self):
        self.assertEqual('1, 2', nice_format((1, 2), use_and=False))

    def test_format_many_str_no_and(self):
        self.assertEqual('1, 2, 3, 4, 5', nice_format((1, 2, 3, 4, 5), use_and=False))

    def test_format_many_mixed(self):
        class Person:
            def __init__(self, first_name: str, last_name: str):
                self.first_name = first_name
                self.last_name = last_name

            def __str__(self):
                return f'{self.first_name} {self.last_name}'

        self.assertEqual('1, two and Alice McBob', nice_format((1, 'two', Person('Alice', 'McBob'))))

    def test_oxford_comma(self):
        self.assertEqual('1, 2, 3, and 4', nice_format((1, 2, 3, 4), oxford_comma=True))


if __name__ == '__main__':
    unittest.main()
