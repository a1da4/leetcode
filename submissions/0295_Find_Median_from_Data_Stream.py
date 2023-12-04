class MedianFinder:

    def __init__(self):
        self._nums = []
        self._numItems = 0

    def addNum(self, num: int) -> None:
        self._nums.append(num)
        self._numItems += 1

    def findMedian(self) -> float:
        self._nums.sort()
        targetId = self._numItems // 2
        if self._numItems % 2:
            return self._nums[targetId]
        else:
            return (self._nums[targetId] + self._nums[targetId - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
