class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        memo = {}

        def search(sId: int, tId: int) -> int:
            if (sId, tId) in memo:
                return memo[(sId, tId)]
            if sId == ns or tId == nt or ns - sId < nt - tId:
                return int(tId == nt)

            answer = search(sId + 1, tId)
            if s[sId] == t[tId]:
                answer += search(sId + 1, tId + 1)
            memo[(sId, tId)] = answer
            return answer

        return search(0, 0)

