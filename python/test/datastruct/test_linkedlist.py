import unittest

from datastruct.linkedlist import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_init_empty(self):
        ll = LinkedList()
        self.assertEqual(0, len(ll))

    def test_init_from_array(self):
        lst = [1, 2, 3, 4, 5]
        ll = LinkedList(lst)
        print(ll)
        self.assertEqual(len(lst), len(ll))
        for index, element in enumerate(ll):
            self.assertEqual(lst[index], element)

    def test_append(self):
        ll = LinkedList()
        self.assertEqual(0, len(ll))
        ll.append(1)
        self.assertEqual(1, len(ll))

    def test_str(self):
        ll = LinkedList()
        self.assertEqual("[]", str(ll))
        ll = LinkedList([1, 2, "3", 4, False])
        self.assertEqual("[1,2,3,4,False]", str(ll))


if __name__ == '__main__':
    unittest.main()
