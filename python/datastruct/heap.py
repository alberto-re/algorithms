class BinaryHeap:
    """Implementation of a binary heap in Python 3."""

    def __init__(self, comparator=lambda x, y: x >= y):
        """
        By default the binary heap behaves as a MaxHeap.

        By providing a custom comparator function it is possible
        to apply a different order criteria.
        """
        self._array = []
        self._comparator = comparator

    def push(self, item):
        """Adds an element to the heap."""
        self._array.append(item)
        self._swim()

    def pop(self):
        """Returns the first element of the heap, and removes it from the collection."""

        # The value to return.
        item = self._array[0]

        # We swap the first element with the latest, then we delete the latter.
        # This way we avoid the O(n) cost of a pop(0) call.
        self._array[0], self._array[-1] = self._array[-1], self._array[0]
        del self._array[-1]

        # Now we sink the new root element until the binary heap order
        # is restored.
        self._sink(0)

        return item

    def peek(self):
        """Returns the first element of the heap, leaving it in place."""
        return self._array[0]

    def _swim(self):
        """Swaps the element at given position with its parent node recursively,
        until the heap total order is restored."""
        item_index = len(self._array) - 1
        if item_index == 0:
            return
        parent_index = self._parent_index(item_index)
        while self._comparator(self._array[item_index], self._array[parent_index]) and item_index > 0:
            self._array[item_index], self._array[parent_index] = self._array[parent_index], self._array[item_index]
            item_index = parent_index
            parent_index = self._parent_index(item_index)

    def _sink(self, index):
        """Swaps the element at given position with its child nodes recursively,
        until the heap total order is restored."""

        # Until there are child nodes for the current one
        while 2 * (index + 1) <= len(self._array):

            # Calculate the left child node's index
            child_index = self._child_index(index)

            # Get the greatest (or smallest, accordingly to the comparator provided) child node's index
            if child_index < len(self._array) - 1 and self._comparator(self._array[child_index + 1], self._array[child_index]):
                child_index += 1

            # If the order between parent and child satisfies the total order we're done
            if self._comparator(self._array[index], self._array[child_index]):
                break

            # Otherwise swap parent and child, then repeat the process
            self._array[index], self._array[child_index] = self._array[child_index], self._array[index]
            index = child_index

    @staticmethod
    def _parent_index(index):
        return ((index + 1) // 2) - 1

    @staticmethod
    def _child_index(index):
        return ((index + 1) * 2) - 1

    def __str__(self):
        return "%s" % self._array
