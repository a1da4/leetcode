class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #return log(n, 3).is_integer() if n > 0 else False
        curr = 1
        if curr == n:
            return True
        while curr < n:
            curr *= 3
            if curr == n:
                return True
        return False

