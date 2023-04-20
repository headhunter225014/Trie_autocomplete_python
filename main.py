import enchant

from SpellChecker import TrieNode


class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.dictionary = enchant.Dict("en_US")

    def insert(self, word):
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_word = True

    def search(self, word):
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_word and self.dictionary.check(word)

    def autocomplete(self, prefix):
        curr_node = self.head
        for char in prefix:
            if char not in curr_node.children:
                return []
            curr_node = curr_node.children[char]

        words = []
        self._dfs(curr_node, prefix, words)
        return words

    def _dfs(self, node, prefix, words):
        if node.is_word and self.dictionary.check(prefix):
            words.append(prefix)
        for char in node.children:
            self._dfs(node.children[char], prefix + char, words)

if __name__ == '__main__':
    trie = Trie()
    with open('/usr/share/dict/american-english') as f:
        english_words = f.read().splitlines()

    for word in english_words:
        trie.insert(word)

    word = input("Enter the first part of the word, the rest will be suggested by autocompletion: ")
    print(trie.autocomplete(word))