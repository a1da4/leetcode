class MedianFinder:

    def __init__(self):
        self._maxNums = []
        heapq.heapify(self._maxNums)
        self._minNums = []
        heapq.heapify(self._minNums)
        
    def addNum(self, num: int) -> None:
        if len(self._minNums) > 0 and num > -1 * self._minNums[0]:
            heapq.heappush(self._maxNums, num)
            if len(self._maxNums) > len(self._minNums):
                _num = heapq.heappop(self._maxNums)
                heapq.heappush(self._minNums, -1 * _num)
        else:
            heapq.heappush(self._minNums, -1 * num)
            if len(self._minNums) - len(self._maxNums) > 1:
                _num = heapq.heappop(self._minNums)
                heapq.heappush(self._maxNums, -1 * _num)
        
    def findMedian(self) -> float:
        if len(self._maxNums) == len(self._minNums):
            return (-1 * self._minNums[0] + self._maxNums[0]) / 2
        else:
            return -1 * self._minNums[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
