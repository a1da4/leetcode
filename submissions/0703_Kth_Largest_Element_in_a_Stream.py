class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(val)
        elif val <= self.nums[0]:
            self.nums.insert(0, val)
        elif val >= self.nums[-1]:
            self.nums.append(val)
        else:
            insertId = 0
            while val > self.nums[insertId]:
                insertId += 1
            self.nums.insert(insertId, val)

        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
