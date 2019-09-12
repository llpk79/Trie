"""A Trie data structure for storing and accessing a corpus of strings.

Use for fast retrieval of strings from a given prefix."""


class Node(object):
    """A node of the Trie tree.

    :var self.char: str -- Character stored at Node.
    :var self.children: dict -- {Node.char: Node}
    :var self.word: bool -- Marks end of word.

    """

    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.word = False  # Marks completion of a word.

    def add(self, child_node):
        """Add child node to children dict.

        :var child_node: 'Node'
        """
        self.children[child_node.char] = child_node


class Trie(object):
    """A Trie.

    :var self.root: 'Node'

    Use insert method to add words to Trie.
    Query Trie by entering a prefix string.

    >>> trie = Trie()
    >>> trie.insert('word or phrase')
    >>> trie.insert('word and similar phrase')
    >>> trie.insert('word')
    >>> trie.insert('woken')

    >>> trie.list_words('wor')
    ['word', 'word and similar phrase', 'word or phrase']

    >>> trie.list_words('wo')
    ['woken', 'word', 'word and similar phrase', 'word or phrase']

    """

    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        """Helper function to call _insert with root node.

        :var word: str
        """
        if not word:
            return
        self._insert(word, self.root)

    def _insert(self, word, node):
        """Recurse through tree.

        Add nodes when current character not on path, mark word completed at end of word.

        :var word: str
        :var node: 'Node'
        """
        # Done adding word, mark this node as a completed word.
        if not word:
            node.word = True
            return node
        # If this character is on the path of a word already in the Trie, carry on.
        elif node.children.get(word[0]):
            return self._insert(word[1:], node.children[word[0]])
        # If a new node needs to be created for this character, go ahead and do it.
        else:
            new_node = Node(word[0])
            node.add(new_node)
            return self._insert(word[1:], new_node)

    def _has_prefix(self, prefix, node):
        """Recurse tree to end of prefix, return None if not contained in tree.

        :var prefix: str
        :var node: 'Node'
        """
        # End of prefix found, return the node.
        if not prefix:
            return node
        # Next character in prefix found, carry on.
        if node.children.get(prefix[0]):
            return self._has_prefix(prefix[1:], node.children[prefix[0]])
        # Tree does not contain any entries containing prefix.
        return None

    def list_words(self, prefix):
        """Helper function to find node at end of prefix and call recursion with that node.

        :var prefix: str
        """
        # Find node at end of prefix.
        node = self._has_prefix(prefix, self.root)
        if node:
            return self._list_words(prefix, node)
        # If prefix not in tree:
        return []

    def _list_words(self, prefix, node, word_list=None):
        """Recurse tree and build word list.

        :var prefix: str
        :var node: 'Node'
        :var word_list: list or None
        """
        # Start with empty list.
        word_list = word_list if word_list is not None else []
        # Word is complete, add to list.
        if node.word:
            word_list.append(prefix)
        # Recurse entire subtree.
        for char in node.children:
            if not node.children[char]:
                word_list.append(prefix + char)
            else:
                self._list_words(prefix + char,
                                 node.children[char],
                                 word_list)
        return word_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
