class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        items = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                num_i = arr[i]
                num_j = arr[j]
                heapq.heappush(items, (num_i/num_j, [num_i, num_j]))

        for _ in range(k - 1):
            heapq.heappop(items)
        
        _, ans = heapq.heappop(items)

        return ans
