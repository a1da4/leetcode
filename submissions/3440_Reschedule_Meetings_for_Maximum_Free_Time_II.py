class Solution:
    def maxFreeTime(
        self, 
        eventTime: int, 
        startTime: List[int], 
        endTime: List[int],
    ) -> int:
        answer = 0
        n = len(startTime)
        freeTime = [0] * (n + 1)
        freeTime[0] = startTime[0]
        freeTime[n] = eventTime - endTime[n - 1]
        for t in range(1, n):
            freeTime[t] = startTime[t] - endTime[t - 1]

        leftMax = [0] * (n + 1)
        for t in range(1, n + 1):
            leftMax[t] = max(leftMax[t - 1], freeTime[t - 1])

        rightMax = [0] * (n + 1)
        for t in range(n - 1, -1, -1):
            rightMax[t] = max(rightMax[t + 1], freeTime[t + 1])        
        
        answer = max(freeTime)

        for t in range(n):
            span = endTime[t] - startTime[t]
            available = freeTime[t] + freeTime[t + 1]

            if span <= max(leftMax[t], rightMax[t+1]):
                available += span
            answer = max(answer, available)

        return answer

