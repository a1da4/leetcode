class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        answer = 0
        costs = [abs(ord(_s) - ord(_t)) for _s, _t in zip(s, t)]
        startId = 0
        curr = 0

        if min(costs) <= maxCost:
            for currId in range(len(s)):
                curr += costs[currId]
                while curr > maxCost:
                    curr -= costs[startId]
                    startId += 1

                answer = max(answer, currId - startId + 1)

        return answer
