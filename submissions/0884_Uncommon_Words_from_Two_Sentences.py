class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        v1 = set(s1.split())
        c1 = Counter(s1.split())
        v2 = set(s2.split())
        c2 = Counter(s2.split())

        return [w for w in v1 ^ v2 if c1[w] == 1 or c2[w] == 1]

