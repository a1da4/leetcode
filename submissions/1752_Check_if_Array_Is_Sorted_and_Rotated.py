class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        head, tail = min(nums), max(nums)
        for currId in range(N):
            nextId = currId + 1 if currId < N - 1 else 0
            if nums[currId] <= nums[nextId] or \
                (nums[currId] == tail and nums[nextId] == head):
                continue
            
            else:
                return False
        
        return True
