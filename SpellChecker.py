#Made By Damir Zababuryn
#04/17/2023


import nltk
from nltk.corpus import words

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


#Initialize the Trie with empty head
class Trie:
    def __init__(self):
        self.head = TrieNode()

    #inserts strings partially adding char to the Trie
    def insert(self, word):

        #set the starting node to the head of the Trie
        curr_node = self.head

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        #for the last character in the string set the node value is_word to true
        curr_node.is_word = True


    #search for a word in a Trie
    def search(self, word):
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_word

    def autocomplete(self, prefix):
        curr_node = self.head
        # Traverse the Trie to the node corresponding to the prefix
        for char in prefix:
            if char not in curr_node.children:
                return []
            curr_node = curr_node.children[char]

        # Collect all words that start with the prefix using a depth-first search
        def dfs(node, prefix, words):
            if node.is_word:
                words.append(prefix)
            for char in node.children:
                dfs(node.children[char], prefix + char, words)

        words = []
        dfs(curr_node, prefix, words)
        return words



if __name__ == '__main__':
    nltk.download('words')
    english_words = words.words()
    # Example usage:
    trie = Trie()

    for word in english_words:
        trie.insert(word)

    word = input("Enter the first part of the word, the rest will be suggested by autocompletiton: ")
    print(trie.autocomplete(word))