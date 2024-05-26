class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals) <= 1:
            return True
        currInterval = intervals[0]
        for nextInterval in intervals[1:]:
            if currInterval[0] <= nextInterval[0] < currInterval[1]:
                return False
            currInterval = nextInterval
        return True

