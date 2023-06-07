class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        targetId = 0
        for sourceId in range(len(s)):
            while s[sourceId] != t[targetId]:
                targetId += 1
                if targetId == len(t):
                    return False
            # s[sourceId] == t[targetId]
            targetId += 1
            if sourceId < len(s) - 1 and targetId == len(t):
                return False
            continue

        return True
