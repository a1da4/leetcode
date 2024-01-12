class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        s = s.lower()
        c1 = Counter(s[:N//2])
        c2 = Counter(s[N//2:])
        v1 = 0
        v2 = 0
        for vowel in ['a', 'i', 'u', 'e', 'o']:
            v1 += c1[vowel]
            v2 += c2[vowel]
        return v1 == v2
