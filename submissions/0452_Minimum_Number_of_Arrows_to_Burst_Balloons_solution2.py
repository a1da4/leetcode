class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for (newS, newE) in points:
            if newS > end:
                end = newE
                arrow += 1
        return arrow
