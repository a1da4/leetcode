class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            heapq.heappush(self.nums, num)

            if len(self.nums) > k:
                heapq.heappop(self.nums)
 
    def add(self, val: int) -> int:
        if len(self.nums) < self.k or self.nums[0] < val:
            heapq.heappush(self.nums, val)

            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
        
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

