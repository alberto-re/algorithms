import unittest

from datastruct.linkedlist import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_init_empty(self):
        ll = LinkedList()
        self.assertEqual([], list(ll))

    def test_init_from_array(self):
        lst = [1, 2, 3, 4, 5]
        ll = LinkedList(lst)
        self.assertEqual(lst, list(ll))

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual([1, 2, 3], list(ll))

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        self.assertEqual([3, 2, 1], list(ll))

    def test_str(self):
        ll = LinkedList()
        self.assertEqual("[]", str(ll))
        ll = LinkedList([1, 2, "3", 4, False])
        self.assertEqual("[1, 2, 3, 4, False]", str(ll))


if __name__ == '__main__':
    unittest.main()
