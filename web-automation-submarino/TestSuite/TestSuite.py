from unittest import TestLoader, TestSuite, TextTestRunner
from Scripts.SearchTest import SearchTestCase
from Scripts.CartTest import CartTestCase

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SearchTestCase),
        loader.loadTestsFromTestCase(CartTestCase)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
