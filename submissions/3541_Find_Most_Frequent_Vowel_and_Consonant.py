class Solution:
    def maxFreqSum(self, s: str) -> int:
        v2f = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        c2f = {}
        vMax, cMax = 0, 0

        for ch in s:
            if ch in v2f:
                v2f[ch] += 1
                vMax = max(v2f[ch], vMax)
            else:
                if ch not in c2f:
                    c2f[ch] = 0
                c2f[ch] += 1
                cMax = max(c2f[ch], cMax)

        return vMax + cMax

