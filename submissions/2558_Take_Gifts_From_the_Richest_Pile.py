class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        for i in range(k):
            _gift = heapq.heappop(heap)
            remained = int(math.sqrt(-_gift))
            heapq.heappush(heap, -remained)
        
        return -sum(heap)

