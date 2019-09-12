# Trie

A python implementation of the Trie data structure.

A Trie data structure is for rapid retrieval of strings from a collection of strings given a prefix.

```
>>>trie = Trie()

# Insert a single word or phrase.
>>>trie.insert('word')
>>>trie.insert('single word or phrase')
# Insert an iterable.
>>>words = ['list', 
            'of', 
            'some', 
            'words', 
            'sometimes', 
            'a',
            'similar',
            'one']:
>>>trie.insert(words)

>>>trie.list_words('wo')
['word', 'words']
>>>trie.list_words('so')
['some', 'sometimes']
>>>trie.list_words('si')
['similar', 'single word or phrase']
```