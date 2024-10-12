class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))
        events.sort(key=lambda x: (x[0], x[1]))

        currIntervals = 0
        maxIntervals = 0
        for event in events:
            currIntervals += event[1]
            maxIntervals = max(maxIntervals, currIntervals)

        return maxIntervals
