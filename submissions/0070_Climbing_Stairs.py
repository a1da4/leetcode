class Solution:
    def climbStairs(self, n: int) -> int:
        num2way = {1:1, 2:2}
        for currNum in range(3, n + 1):
            num2way[currNum] = num2way[currNum - 1] + num2way[currNum - 2]
        
        return num2way[n]
