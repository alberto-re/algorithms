from typing import Dict


class TrieNode:

    def __init__(self, char: str = None, is_word: bool = False) -> None:
        self._char: str = char
        self._is_word: bool = is_word
        self._children: Dict[str, TrieNode] = {}

    def child(self, char: str) -> "TrieNode":
        if char in self._children:
            return self._children[char]
        return None

    def add_child(self, char: str) -> None:
        self._children[char] = TrieNode(char)

    @property
    def is_word(self) -> bool:
        return self._is_word

    @is_word.setter
    def is_word(self, truth: bool) -> None:
        self._is_word = truth


class Trie:

    def __init__(self) -> None:
        self._root: TrieNode = TrieNode()

    def contains(self, item: str) -> bool:
        child: TrieNode = self._root
        for char in item:
            child = child.child(char)
            if child is None:
                return False
        return child.is_word

    def add(self, item: str) -> None:
        child: TrieNode = self._root
        for char in item:
            if child.child(char) is None:
                child.add_child(char)
            child = child.child(char)
        child.is_word = True


if __name__ == "__main__":
    trie = Trie()
    print("trie.contains(\"dog\")?", trie.contains("dog"))
    trie.add("dog")
    print("trie.contains(\"dog\")?", trie.contains("dog"))
    print("trie.contains(\"do\")?", trie.contains("do"))
