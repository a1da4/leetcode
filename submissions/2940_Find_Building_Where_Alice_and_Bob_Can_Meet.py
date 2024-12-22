class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N = len(heights)
        ans = [-1] * len(queries)
        
        targetQueries = [[] for _ in heights]
        for qId, query in enumerate(queries):
            a, b = query
            if a > b:
                a, b = b, a
            
            if heights[a] < heights[b]:
                ans[qId] = b
            elif a == b:
                ans[qId] = a
            else:
                targetQueries[b].append(
                    (max(heights[a], heights[b]), qId)
                )
        
        heap = []
        for hId, height in enumerate(heights):
            while heap and heap[0][0] < height:
                _, qId = heapq.heappop(heap)
                ans[qId] = hId
            for item in targetQueries[hId]:
                heapq.heappush(heap, item)

        return ans

