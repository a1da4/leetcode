class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        answer = 0
        preSum = 0
        sortedPreSum = 0

        for i in range(len(arr)):
            preSum += arr[i]
            sortedPreSum += i
            if preSum == sortedPreSum:
                answer += 1

        return answer

