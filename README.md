# Trie

A python implementation of the Trie data structure.

A Trie data structure is for rapid retrieval of strings from a collection of strings given a prefix.


##### Instantiate a Trie
```
>>>trie = Trie()
```

##### Insert a single string.
```
>>>trie.insert('word')
>>>trie.insert('single word or phrase')
```
##### Insert an iterable of strings.
```
>>>words = ['list', 
            'of', 
            'some', 
            'words', 
            'sometimes', 
            'a',
            'similar',
            'one']:
>>>trie.insert(words)
```
##### Retrieve list of stings beginning with given prefix.
```
>>>trie.list_words('wo')
['word', 'words']

>>>trie.list_words('so')
['some', 'sometimes']

>>>trie.list_words('si')
['similar', 'single word or phrase']
```