class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        numArrows = 0
        thresh = -inf
        for start, end in points:
            if thresh >= start:
                pass
            else:
                thresh = end
                numArrows += 1 
        
        return numArrows
