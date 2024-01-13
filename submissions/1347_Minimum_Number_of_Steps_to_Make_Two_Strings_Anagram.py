class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum([c for c in (Counter(t) - Counter(s)).values()])
