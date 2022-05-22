class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        self.trie[word[0]] = self.trie.get(word[0], []) + [word]

    def search(self, word: str) -> bool:
        return word in self.trie.get(word[0], [])

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie.get(prefix[0], []):
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)