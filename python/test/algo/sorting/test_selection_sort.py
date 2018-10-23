import unittest

from algo.sorting.selection_sort import sort
from test.algo.abc_sort import BaseSortTest


class SelectionSortTest(BaseSortTest, unittest.TestCase):

    def _sort(self, collection):
        return sort(collection)


if __name__ == '__main__':
    unittest.main()
