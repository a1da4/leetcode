class Trie:

    def __init__(self):
        self.items = set()
        self.starts = set()

    def insert(self, word: str) -> None:
        self.items.add(word)
        ch = ""
        for currId in range(len(word)):
            ch += word[currId]
            if ch not in self.starts:
                self.starts.add(ch)

    def search(self, word: str) -> bool:
        return word in self.items

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.starts


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
