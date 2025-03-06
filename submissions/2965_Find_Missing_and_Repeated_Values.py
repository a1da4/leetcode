class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num2freq = {num: 0 for num in range(1, len(grid) ** 2 + 1)}
        for row in grid:
            for num in row:
                num2freq[num] += 1
        
        a, b = None, None
        for num, freq in num2freq.items():
            if freq == 2:
                a = num
            if freq == 0:
                b = num

        return [a, b]
