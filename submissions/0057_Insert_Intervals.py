class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        numIntervals = len(intervals)  
        if numIntervals == 0:
            return [newInterval]

        # insert first
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        answer = []
        start = None
        finished = False
        for intervalId in range(numIntervals):
            if finished:
                answer.append(intervals[intervalId])
                continue
            
            # insert
            if intervalId < numIntervals - 1 and intervals[intervalId][1] < newInterval[0] <= newInterval[1] < intervals[intervalId+1][0]:
                answer.append(intervals[intervalId])
                answer.append(newInterval)
                finished = True
                continue

            # pass
            if start == None and (intervals[intervalId][0] > newInterval[1] or
                intervals[intervalId][1] < newInterval[0]):
                answer.append(intervals[intervalId])
                continue

            # newInterval is included intervals[intervalId]
            if intervals[intervalId][0] <= newInterval[0] <= newInterval[1] <= intervals[intervalId][1]:
                return intervals

            # define start
            if newInterval[0] <= intervals[intervalId][0] and start == None:
                start = newInterval[0]
            if intervals[intervalId][0] <= newInterval[0] and start == None:
                start = intervals[intervalId][0]

            # define end
            if start != None and intervals[intervalId][0] <= newInterval[1] <= intervals[intervalId][1]:
                answer.append([start, intervals[intervalId][1]])
                finished = True
            if start != None and newInterval[1] < intervals[intervalId][0]:
                answer.append([start, newInterval[1]])
                answer.append(intervals[intervalId])
                finished = True

        #insert last
        if finished is False:
            if start is None:
                answer.append(newInterval)
            else:
                answer.append([start, newInterval[1]])
                
        return answer
