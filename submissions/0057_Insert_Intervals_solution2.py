class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        answer = []
        currId = 0
        numIntervals = len(intervals)
        
        while currId < numIntervals and intervals[currId][1] < newInterval[0]:
            answer.append(intervals[currId])
            currId += 1

        if currId < numIntervals:
            newInterval[0] = min(newInterval[0], intervals[currId][0])
        while currId < numIntervals and intervals[currId][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[currId][1])
            currId += 1
        answer.append(newInterval)

        if currId < numIntervals:
            return answer + intervals[currId:]
        else:
            return answer
