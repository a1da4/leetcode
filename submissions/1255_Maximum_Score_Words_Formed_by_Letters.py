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
        self.maxScore = 0

        def is_valid(currCounter) -> bool:
            if any([key not in refCounter for key in currCounter.keys()]):
                return False
            if any([freq > 0 for freq in (currCounter - refCounter).values()]):
                return False
            return True

        def search(currId: int, currScore: int, currCounter):
            for nextId in range(currId + 1, N):
                nextCounter = Counter(words[nextId])
                if is_valid(currCounter + nextCounter):
                    self.maxScore = max(self.maxScore, currScore + scores[nextId])
                    search(nextId, currScore + scores[nextId], currCounter + nextCounter)

        search(-1, 0, Counter())

        return self.maxScore

