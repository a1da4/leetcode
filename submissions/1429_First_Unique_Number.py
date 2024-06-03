class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = deque(nums)
        self.num2unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.nums and not self.num2unique[self.nums[0]]:
            self.nums.popleft()
        if self.nums:
            return self.nums[0]
        return -1

    def add(self, value: int) -> None:
        if value not in self.num2unique:
            self.num2unique[value] = True
            self.nums.append(value)
        else:
            self.num2unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
