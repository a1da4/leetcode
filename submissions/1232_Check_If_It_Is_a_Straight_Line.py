class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = None
        coordinates.sort()
        for point1, point2 in zip(coordinates[:-1], coordinates[1:]):
            gcd = math.gcd((point2[1] - point1[1]), (point2[0] - point1[0]))
            currSlope = ((point2[1] - point1[1]) / gcd, (point2[0] - point1[0]) / gcd)

            if slope is None:
                slope = currSlope
            else:
                if slope[0] == currSlope[0] == 0 or slope[1] == currSlope[1] == 0:
                    continue 
                if slope != currSlope:
                    return False
        return True

