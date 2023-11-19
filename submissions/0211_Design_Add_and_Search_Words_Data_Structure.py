class WordDictionary:

    def __init__(self):
        self.vocab = set()
        self.words = []

    def addWord(self, word: str) -> None:
        self.vocab.add(word)
        self.words.append(word)

    def _exclude_dots(self, word: str, dotIds: List[int]) -> str:
        currWord = ""
        currId = 0
        for dotId in dotIds:
            currWord += word[currId:dotId]
            currId = dotId+1
        currWord += word[currId:]
        return currWord

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.vocab
        else:
            dotIds = [i for i in range(len(word)) if word[i]=="."]
            target = self._exclude_dots(word, dotIds)
            numChars = len(word)
            for reference in self.words:
                if len(reference) != numChars:
                    continue
                reference = self._exclude_dots(reference, dotIds)
                if target == reference:
                    return True
            
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
