class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        answer = []
        queue = deque()

        for currId in range(k):
            while queue and nums[queue[-1]] <= nums[currId]:
                queue.pop()
            queue.append(currId)
        answer.append(nums[queue[0]])

        for currId in range(k, N):
            if currId - queue[0] >= k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[currId]:
                queue.pop()
            queue.append(currId)
            answer.append(nums[queue[0]])

        return answer
