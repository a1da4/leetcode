class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # consider len(nums1) * len(nums2) < k
        if len(nums1) * len(nums2) < k:
            return [[num1, num2] for num1 in nums1 for num2 in nums2]

        from heapq import heappush, heappop

        N1 = len(nums1)
        N2 = len(nums2)

        results = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (id1, id2) = heappop(minHeap)
            results.append([nums1[id1], nums2[id2]])

            if id1 + 1 < N1 and (id1 + 1, id2) not in visited:
                heappush(minHeap, (nums1[id1 + 1] + nums2[id2], (id1 + 1, id2)))
                visited.add((id1 + 1, id2))
            if id2 + 1 < N2 and (id1, id2 + 1) not in visited:
                heappush(minHeap, (nums1[id1] + nums2[id2 + 1], (id1, id2 + 1)))
                visited.add((id1, id2 + 1))
            k -= 1
        
        return results
