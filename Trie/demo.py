from Trie import Trie


def main():
    """A quick demo of Trie insert and list_words methods."""

    # Instantiate an empty Trie.
    trie = Trie()

    # Add individual words.
    trie.insert('word')

    # Add phrases.
    trie.insert('Any old phrase, any length.')
    trie.insert('will do.')

    # Add iterables.
    print(f'Add 466551 words to the Trie...')
    with open('../words.txt', 'r') as f:
        text = [word.strip() for word in f.readlines()]
    trie.insert(text)

    print('Find strings starting with:')
    print(f"any: {trie.list_words('any')}")
    print(f"prefix: {trie.list_words('prefix')}")
    print(f"will do: {trie.list_words('will do')}")


if __name__ == "__main__":
    main()
