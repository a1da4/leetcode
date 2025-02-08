class NumberContainers:
    def __init__(self):
        self.num2ids = defaultdict(list)
        self.id2nums = {}

    def change(self, index: int, number: int) -> None:
        self.id2nums[index] = number
        heapq.heappush(self.num2ids[number], index)

    def find(self, number: int) -> int:
        if not self.num2ids[number]:
            return -1

        while self.num2ids[number]:
            index = self.num2ids[number][0]

            if self.id2nums.get(index) == number:
                return index
            heapq.heappop(self.num2ids[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
