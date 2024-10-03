class Solution:
    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0

        if value > index:
            count += (value - index) * (index + 1) + (index * (index + 1)) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        
        if value > n - index:
            count += (value - n + 1 + index) * (n - index) + (n - index - 1) * (n - index) // 2

        else:
            count += (value + 1) * value // 2 + n - index - value
        
        return count - value
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 1, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if self.getSum(index, m, n) <= maxSum:
                l = m
            else:
                r = m - 1
        
        return l
