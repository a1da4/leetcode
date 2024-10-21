class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        vocab = set()
        return self.search(s, 0, vocab)

    def search(self, s: str, start: int, vocab: Set[str]) -> int:
        if start == len(s):
            return 0
        
        answer = 0
        for end in range(start + 1, len(s) + 1):
            _s = s[start:end]
            if _s not in vocab:
                vocab.add(_s)
                answer = max(answer, 1 + self.search(s, end, vocab))
                vocab.remove(_s)

        return answer

