class Solution:
    def binarySearch(self, intervals, target, left, right):
        if left >= right:
            if intervals[left][0] >= target:
                return intervals[left]
            return None
        mid = (left + right) // 2
        if intervals[mid][0] < target:
            return self.binarySearch(intervals, target, mid + 1, right)
        else:
            return self.binarySearch(intervals, target, left, mid)

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        
        result = [-1] * N
        interval2id = {tuple(intervals[i]): i for i in range(N)}

        intervals.sort(key=lambda x: x[0])

        for i in range(N):
            interval = self.binarySearch(intervals, intervals[i][1], 0, N-1)
            if interval:
                result[interval2id[tuple(intervals[i])]] = interval2id[tuple(interval)]

        return result

