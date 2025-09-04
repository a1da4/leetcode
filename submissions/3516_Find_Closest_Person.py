class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff = abs(z - x) - abs(z - y)
        if diff == 0:
            return 0
        elif diff < 0:
            return 1
        else:
            return 2 
