class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda x: x[0])
        intervals = deque(intervals)
        prevStart, prevEnd = intervals.popleft()
        while intervals:
            currStart, currEnd = intervals.popleft()
            if currStart <= prevEnd:
                if prevEnd < currEnd:
                    prevEnd = currEnd
            else:
                answer.append([prevStart, prevEnd])
                prevStart = currStart
                prevEnd = currEnd
        if len(answer) == 0 or answer[-1][1] != prevEnd:
            answer.append([prevStart, prevEnd])
        
        return answer
