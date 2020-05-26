import unittest

from algo.sorting.selection_sort import selection_sort
from test.algo.abc_sort import BaseSortTest


class SelectionSortTest(BaseSortTest, unittest.TestCase):

    def _sort(self, collection):
        return selection_sort(collection)


if __name__ == '__main__':
    unittest.main()
