class Solution:
    def maximumLength(self, s: str) -> int:
        count = Counter()
        N = len(s)
        for sId in range(N):
            ch = s[sId]
            subLen = 0
            for eId in range(sId, N):
                if ch == s[eId]:
                    subLen += 1
                    count[(ch, subLen)] += 1
                else:
                    break

        answer = -1
        for key, val in count.items():
            _, subLen = key
            if val >= 3 and subLen > answer:
                answer = subLen

        return answer

