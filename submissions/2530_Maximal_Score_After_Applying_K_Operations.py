class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            _num = heapq.heappop(heap)
            num = -_num
            score += num
            heapq.heappush(heap, - ceil(num / 3))

        return score
