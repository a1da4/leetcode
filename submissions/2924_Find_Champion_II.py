class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()
        for edge in edges:
            losers.add(edge[1])
        
        if len(losers) < n - 1:
            return -1
        else:
            return list(set(range(n)) - losers)[0]

