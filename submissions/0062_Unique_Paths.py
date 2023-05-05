from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numDownToGo = m - 1
        numRightToGo = n - 1
        
        return int(factorial(numDownToGo + numRightToGo) / factorial(numDownToGo) / factorial(numRightToGo))
