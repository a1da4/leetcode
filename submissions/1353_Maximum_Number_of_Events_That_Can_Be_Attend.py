class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        currDay = 0
        answer = 0
        heap = []
        currId = 0
        events.sort(key=lambda x:x[0])
        N = len(events)

        while currId < N or heap:
            if not heap:
                currDay = max(currDay, events[currId][0])
            
            while currId < N and events[currId][0] <= currDay:
                heapq.heappush(heap, events[currId][1])
                currId += 1

            while heap and heap[0] < currDay:
                heapq.heappop(heap)
            
            if not heap:
                continue
            
            heapq.heappop(heap)
            answer += 1
            currDay += 1

        return answer
