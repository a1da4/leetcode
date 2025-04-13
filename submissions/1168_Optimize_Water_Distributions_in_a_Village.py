class Solution:
    def minCostToSupplyWater(
        self, 
        n: int, 
        wells: List[int], 
        pipes: List[List[int]],
    ) -> int:
        parent = [i for i in range(n + 1)]

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True
        
        edges = []
        for i in range(n):
            heapq.heappush(edges, [wells[i], 0, i + 1])
        
        for house1, house2, cost in pipes:
            heapq.heappush(edges, [cost, house1, house2])
        
        num = 0
        answer = 0
        while edges:
            cost, house1, house2 = heapq.heappop(edges)
            if union(house1, house2):
                answer += cost
                num += 1
                if num == n:
                    break

        return answer

