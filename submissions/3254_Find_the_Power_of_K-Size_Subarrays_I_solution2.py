class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        answer = [-1] * (N - k + 1)
        queue = deque()

        for currId in range(N):
            # keep only k items
            if queue and queue[0] < currId - k + 1:
                queue.popleft()
            # verify the "power" condition
            if queue and nums[currId - 1] + 1 != nums[currId]:
                queue.clear()
            queue.append(currId)
            if currId >= k - 1 and len(queue) == k:
                answer[currId - k + 1] = nums[queue[-1]]

        return answer

