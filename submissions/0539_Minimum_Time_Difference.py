class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def convert(time: str) -> int:
            return int(time[:2]) * 60 + int(time[3:])
        
        times = [convert(time) for time in timePoints]
        times.sort()
        answer = min(time_2 - time_1 for time_1, time_2 in zip(times[:-1], times[1:]))

        return min(answer, 24 * 60 - times[-1] + times[0])

