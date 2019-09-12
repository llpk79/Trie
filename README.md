# Trie

A python implementation of the Trie data structure.

A Trie data structure is for rapid retrieval of strings from a collection of strings given prefix.

```
>>>trie = Trie()
>>>for word in ['list', 
                'of', 
                'some', 
                'words', 
                'sometimes', 
                'a',
                'similar',
                'word']:
       trie.insert(word)

>>>trie.list_words('wo')
['word', 'words']
>>>trie.list_words('so')
['some', 'sometimes']
```