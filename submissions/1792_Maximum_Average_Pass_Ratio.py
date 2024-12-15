class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for nPass, nTotal in classes:
            if nPass == nTotal:
                heapq.heappush(heap, (float("inf"), nPass, nTotal))
            else:
                heapq.heappush(heap, ( - (nTotal - nPass) / (nTotal * (nTotal + 1)), nPass, nTotal))

        for _ in range(extraStudents):
            _, nPass, nTotal = heapq.heappop(heap)
            nPass += 1
            nTotal += 1
            heapq.heappush(heap, ( - (nTotal - nPass) / (nTotal * (nTotal + 1)), nPass, nTotal))

        totalRatio = 0
        for _, nPass, nTotal in heap:
            ratio = nPass / nTotal
            totalRatio += ratio

        return totalRatio / len(classes)

