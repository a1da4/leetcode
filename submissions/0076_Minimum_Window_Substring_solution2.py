class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        countW = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        need = len(countT)
        resl = float("inf")
        res = [-1, -1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            countW[c] = countW.get(c, 0) + 1
            if c in countT and countW[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resl:
                    res = [l, r]
                    resl = r - l + 1
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resl != float("inf") else ""
