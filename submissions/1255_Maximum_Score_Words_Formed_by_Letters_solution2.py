class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = []
        for word in words:
            _s = 0
            for ch in word:
                _s += score[ord(ch) - ord('a')]
            scores.append(_s)

        N = len(words)
        refCounter = Counter(letters)
        refVocab = set(letters)
        self.maxScore = 0
        counters = [Counter(word) for word in words]

        def is_valid(currCounter) -> bool:
            for currKey, currFreq in currCounter.items():
                if currKey not in refVocab:
                    return False
                if refCounter[currKey] < currFreq:
                    return False
            return True

        def search(currId: int, currScore: int, currCounter):
            for nextId in range(currId + 1, N):
                nextCounter = counters[nextId]
                if is_valid(currCounter + nextCounter):
                    self.maxScore = max(self.maxScore, currScore + scores[nextId])
                    search(nextId, currScore + scores[nextId], currCounter + nextCounter)

        search(-1, 0, Counter())

        return self.maxScore

