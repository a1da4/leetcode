class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque()
        count = 0
        N = len(nums)
        for currId in range(N):
            while queue and currId > queue[0] + 2:
                queue.popleft()
            
            if (nums[currId] + len(queue)) % 2:
                continue
            
            if currId + 2 >= N:
                return -1
            
            count += 1
            queue.append(currId)
        
        return count

