class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id2heap = {}
        for item in items:
            _id, score = item
            if _id not in id2heap:
                id2heap[_id] = []
            heapq.heappush(id2heap[_id], -score)
        
        answer = []
        for _id in sorted(id2heap.keys()):
            heap = id2heap[_id]
            _sum = 0
            for _ in range(5):
                _sum += - heapq.heappop(heap)
            
            answer.append([_id, int(_sum / 5)])
        
        return answer
