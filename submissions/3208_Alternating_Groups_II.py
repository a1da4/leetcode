class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        answer = 0
        currCount = 1
        prevColor = colors[0]

        for i in range(1, N + k - 1):
            currId = i % N

            if prevColor == colors[currId]:
                currCount = 1
                continue
            
            currCount += 1
            if currCount >= k:
                answer += 1
            prevColor = colors[currId]

        return answer

