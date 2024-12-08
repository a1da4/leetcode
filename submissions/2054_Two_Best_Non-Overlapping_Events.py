class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        N = len(events)
        dp = [[-1] * 3 for _ in range(N)]

        def _find(eId: int, count: int):
            if count == 2 or eId >= N:
                return 0
            if dp[eId][count] == -1:
                end = events[eId][1]
                l, r = eId + 1, N - 1
                while l < r:
                    #m = l + ((r - l) >> 1) is more secure
                    m = l + ((r - l) // 2)
                    if events[m][0] > end:
                        r = m
                    else:
                        l = m + 1
                inc = events[eId][2] + (
                    _find(l, count + 1)
                    if l < N and events[l][0] > end
                    else 0
                )
                exc = _find(eId + 1, count)
                dp[eId][count] = max(inc, exc)
            return dp[eId][count]
        
        return _find(0, 0)

