class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for interval in intervals:
            times.append((interval[0], 'start'))
            times.append((interval[1], 'end'))
        
        maxRooms = 0
        currRooms = 0
        for time in sorted(times):
            _, label = time
            if label == 'start':
                currRooms += 1
                maxRooms = max(maxRooms, currRooms)
            else:
                currRooms -= 1
        return maxRooms

