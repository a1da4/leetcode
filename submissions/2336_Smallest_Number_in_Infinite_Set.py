class SmallestInfiniteSet:

    def __init__(self):
        self.present = set()
        self.added = []
        self.current = 1

    def popSmallest(self) -> int:
        if len(self.added):
            answer = heapq.heappop(self.added)
            self.present.remove(answer)
        else:
            answer = self.current
            self.current += 1
        return answer

    def addBack(self, num: int) -> None:
        if num not in self.present and self.current > num:
            heapq.heappush(self.added, num)
            self.present.add(num)
