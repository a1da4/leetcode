class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSum = 1
        rightSum = n * (n + 1) / 2

        if leftSum == rightSum:
            return 1

        for currNum in range(2, n + 1):
            leftSum += currNum
            rightSum -= (currNum - 1)
            if leftSum == rightSum:
                return currNum
        return -1
