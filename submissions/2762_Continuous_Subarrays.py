class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxQueue = deque()
        minQueue = deque()
        left = 0
        answer = 0

        for right, num in enumerate(nums):
            while maxQueue and nums[maxQueue[-1]] < num:
                maxQueue.pop()
            maxQueue.append(right)

            while minQueue and nums[minQueue[-1]] > num:
                minQueue.pop()
            minQueue.append(right)

            while (
                maxQueue 
                and minQueue 
                and nums[maxQueue[0]] - nums[minQueue[0]] > 2
            ):
                if maxQueue[0] < minQueue[0]:
                    left = maxQueue[0] + 1
                    maxQueue.popleft()
                else:
                    left = minQueue[0] + 1
                    minQueue.popleft()

            answer += right - left + 1

        return answer

