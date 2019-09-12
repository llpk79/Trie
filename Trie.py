"""A Trie data structure for storing and accessing a corpus of strings."""
from collections import deque


class Node(object):
    """A node of the Trie tree."""

    def __init__(self, char):
        self.char = char if char else None
        self.children = []  # TODO make this a dict
        self.word = False


class Trie(object):
    """A Trie."""

    def __init__(self):
        self.root = Node(None)

    def add(self, word):
        # TODO: Make recursive
        node = self.root

        for char in word:
            found = False
            for child in node.children:
                if char == child.char:
                    node = child
                    found = True
                    break
            if not found:
                new = Node(char)
                node.children.append(new)
                node = new
        node.word = True

    def words_with_prefix(self, prefix):
        if not self.root.children:
            return None
        node = self.root
        for char in prefix:
            found = False
            for child in node.children:
                if char == child.char:
                    found = True
                    node = child
                    break
            if not found:
                return None
        return node

    def list_with_prefix(self, prefix):
        # TODO: Make recursive
        has_words = self.words_with_prefix(prefix)
        if has_words:
            queue = deque(has_words.children)
        else:
            return None
        words = []
        string = prefix
        print(len(queue))
        while queue:
            node = queue.popleft()
            temp = string + node.char
            if self.words_with_prefix(temp):
                string += node.char
                print(string)
                if node.word:
                    words.append(string)
            queue.extend(node.children)
        return words


if __name__ == "__main__":
    trie = Trie()
    # with open('words.txt', 'r') as f:
    #     text = f.readlines()
    #
    # for word in text[150:200]:
    #     # print(word.strip())
    #     trie.add(word.strip())
    trie.add('hack')
    trie.add('hacker')
    trie.add('hacking')

    print(trie.list_with_prefix('hac'))
    # print(trie.list_with_prefix('cor'))
    # print(trie.list_with_prefix('stra'))
    # print(trie.list_with_prefix('thin'))
    # print(trie.list_with_prefix('base'))
