class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        numWords = len(words)
        wordFreq = Counter("".join(words))

        for word, freq in wordFreq.items():
            if freq % numWords > 0:
                return False
        
        return True
