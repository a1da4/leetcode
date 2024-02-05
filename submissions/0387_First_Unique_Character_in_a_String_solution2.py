class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for currId, currS in enumerate(s):
            if c[currS] == 1:
                return currId

        return -1
