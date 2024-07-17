class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        nums = deque(nums)
        curr = nums.popleft()
        while nums:
            num = nums.popleft()
            diff = num - curr - 1
            if diff >= k:
                return curr + k
            k -= diff
            curr = num
        
        return curr + k
