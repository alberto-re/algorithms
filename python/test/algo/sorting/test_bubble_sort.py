import unittest

from algo.sorting.bubble_sort import sort
from test.algo.abc_sort import BaseSortTest


class BubbleSortTest(BaseSortTest, unittest.TestCase):

    def _sort(self, collection):
        return sort(collection)


if __name__ == '__main__':
    unittest.main()
