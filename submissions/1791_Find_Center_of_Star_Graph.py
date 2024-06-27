class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        answer = set(edges[0]) & set(edges[1])
        return answer.pop()
