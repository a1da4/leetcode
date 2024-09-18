class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w2c = Counter(f"{s1} {s2}".split())
        return [w for w, c in w2c.items() if c == 1]

