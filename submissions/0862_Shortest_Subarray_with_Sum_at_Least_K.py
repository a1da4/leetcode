class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        answer = float("inf")

        currSum = 0
        heap = []

        for currId, num in enumerate(nums):
            currSum += num

            if currSum >= k:
                answer = min(answer, currId + 1)

            while heap and currSum - heap[0][0] >= k:
                answer = min(answer, currId - heappop(heap)[1])

            heappush(heap, (currSum, currId))

        if answer == float("inf"):
            return -1
        else:
            return answer

