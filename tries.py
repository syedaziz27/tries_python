class TrieNode:
    def __init__(self, val):
        self.val = val  # current node value
        self.parent = None  # keeps track of parent node
        self.children = {}  # dict that holds all children nodes
        # used to determine if current node is last letter in a specified a word
        self.endOfWord = False


class Trie:
    def __init__(self):  # initializes Trie instance with root that is a TrieNode with value None
        self.root = TrieNode(None)

    def __repr__(self):  # Represents Trie instance by describing root's children
        return f'Root of trie with the following children: {list(self.root.children.keys())}'

    def add_word(self, word):  # Add a word to trie
        node = self.root       # Defines node that will traverse trie
        i = 0
        for i in range(0, len(word)):   # loop through each character in word
            char = word[i]
            if char not in node.children:
                # Add letter to children obj if it isn't there
                node.children.update({char: TrieNode(char)})
                # Give child node reference to it's parent node, or prev letter in word
                node.children[char].parent = node

            # Move to the child node that is the current letter
            node = node.children[char]

            # check to see if end of word has been reached, will mark node as the end of a word
            if i == len(word) - 1:
                node.endOfWord = True

    def contains_word(self, word):
        node = self.root     # Defines node that will traverse trie
        for char in word:
            if (char not in node.children):
                return False  # returns false if char not in current node's children
            else:
                # move on to the node the has the val of current char in order to see if its children contain the next letter
                node = node.children[char]
        return True    # will occur if each char is a node in trie and each node with val of char has the next letter in word in its children dict


word_trie = Trie()
word_trie.add_word('cat')
word_trie.add_word('car')
word_trie.add_word('call')
word_trie.add_word('catfish')
word_trie.add_word('ball')
word_trie.add_word('balloon')

print(word_trie.contains_word('cat'))   # True
print(word_trie.contains_word('dog'))   # False
print(word_trie)    # Returns message in __repr__ method
