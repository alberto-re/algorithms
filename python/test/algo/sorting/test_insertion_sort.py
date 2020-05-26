import unittest

from algo.sorting.insertion_sort import insertion_sort
from test.algo.abc_sort import BaseSortTest


class InsertionSortTest(BaseSortTest):

    def _sort(self, collection):
        return insertion_sort(collection)


if __name__ == '__main__':
    unittest.main()
