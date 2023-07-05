class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0
        for diff in gain:
            current += diff
            highest = max(current, highest)
        
        return highest
