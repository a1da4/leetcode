class Solution:
    def repairCars(self, rank: List[int], cars: int) -> int:
        count = Counter(rank)
        heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(heap)

        while cars > 0:
            time, rank, n, count = heappop(heap)
            cars -= count
            n += 1
            heappush(heap, [rank * n * n, rank, n, count])

        return time

