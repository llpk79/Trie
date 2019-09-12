from Trie import Trie


def main():
    """A quick demo of Trie insert and list_words methods."""
    print(f'Add 466551 words to the Trie...')

    # Instantiate an empty Trie.
    trie = Trie()
    with open('words.txt', 'r') as f:
        text = f.readlines()
    # Add a bunch of words.
    for word in text:
        trie.insert(word.strip())

    print('Find words starting with:')
    print(f"worm: {trie.list_words('worm')}")
    print(f"corp: {trie.list_words('corp')}")
    print(f"strap: {trie.list_words('strap')}")
    print(f"thing: {trie.list_words('thing')}")
    print(f"basec: {trie.list_words('basec')}")


if __name__ == "__main__":
    main()
