class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda x: x[0])
        prevStart, prevEnd = intervals[0]
        for interval in intervals[1:]:
            currStart, currEnd = interval
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
