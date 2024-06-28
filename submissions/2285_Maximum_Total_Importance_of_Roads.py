class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance = [0] * n
        for road in roads:
            importance[road[0]] += 1
            importance[road[1]] += 1

        importance.sort()
        answer = 0
        value = 1
        for imp in importance:
            answer += value * imp
            value += 1

        return answer

