class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxLength = 0

    def addWord(self, word: str) -> None:
        node = self.root
        length = 0
        for char in word:
            if char not in node.links:
                node.links[char] = TrieNode()
            node = node.links[char]
            length += 1
        self.maxLength = max(self.maxLength, length)
        node.end = True

    def search(self, word: str) -> bool:
        if len(word) > self.maxLength:
            return False
        
        def _helper(id, node):
            for currId in range(id, len(word)):
                char = word[currId]
                if char == ".":
                    for nextNode in node.links.values():
                        if _helper(currId+1, nextNode):
                            return True
                    return False
                else:
                    if char not in node.links:
                        return False
                    node = node.links[char]
            return node.end
        
        return _helper(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
