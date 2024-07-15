class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            curr = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, curr)
            cost += curr

        return cost

