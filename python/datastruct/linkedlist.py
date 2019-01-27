from typing import Any, List, Optional


class Node:
    """A node object. It consists of a value and a reference
    to the next element in the list."""

    def __init__(self, value: Any, nxt: 'Node' = None) -> None:
        self._value = value
        self._next = nxt

    @property
    def value(self) -> Any:
        return self._value

    @property
    def next(self) -> Any:
        return self._next

    @next.setter
    def next(self, next_node: 'Node') -> None:
        self._next = next_node

    def __str__(self) -> str:
        return str(self._value)


class LinkedList:
    """A singly-linked linked list data structure."""

    def __init__(self, array: List[Any] = None) -> None:
        self._head: Optional[Node] = None
        self._len = 0
        if array is not None:
            for element in array:
                self._append(element)
        self._cur_node: Optional[Node] = None

    def is_empty(self) -> bool:
        """Is the list empty?"""
        return self._head is None

    def append(self, value: Any) -> None:
        """Adds an element to the end of the list."""
        self._append(value)

    def prepend(self, value: Any) -> None:
        """Adds an element to the beginning of the list."""
        if self._head is not None:
            second = self._head
            self._head = Node(value, second)
        else:
            self._head = Node(value)
        self._len += 1

    def _append(self, value: Any) -> None:
        if self._head is not None:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(value)
        else:
            self._head = Node(value)
        self._len += 1

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> 'LinkedList':
        self._cur_node = None
        return self

    def __next__(self) -> Any:
        if self._cur_node:
            self._cur_node = self._cur_node.next
        else:
            self._cur_node = self._head
        if self._cur_node is None:
            raise StopIteration
        return self._cur_node.value

    def __str__(self) -> str:
        values = []
        if self._head:
            cur = self._head
            values.append(cur.value)
            while cur.next is not None:
                cur = cur.next
                values.append(cur.value)
        return "[" + ", ".join(map(str, values)) + "]"
