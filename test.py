import unittest
from Trie import Trie


# TODO: Add more stringent tests
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert(self):
        strings = ['this', 'that', 'the other']
        for string in strings:
            self.trie.insert(string)
        self.assertListEqual(self.trie.list_words('th'), strings)

    def test_retrieve(self):
        strings = ['this', 'that', 'the other']
        for string in strings:
            self.trie.insert(string)
        self.assertListEqual(self.trie.list_words('th'), strings)


if __name__ == '__main__':
    unittest.main()
