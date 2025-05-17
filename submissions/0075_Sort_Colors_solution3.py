class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _nums = []
        heapq.heapify(nums)
        while nums:
            _nums.append(
                heapq.heappop(nums)
            )
        
        nums[:] = _nums
