class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        thresh = - inf
        numRemove = 0
        for start, end in intervals:
            if start >= thresh:
                thresh = end
            else:
                numRemove += 1
        
        return numRemove
