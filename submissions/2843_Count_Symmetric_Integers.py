class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def verify(num: int) -> bool:
            numStr = str(num)
            N = len(numStr)
            if N % 2:
                return False
            N //= 2
            left = sum([int(numCh) for numCh in numStr[:N]])
            right = sum([int(numCh) for numCh in numStr[-N:]])
            return left == right
        
        return sum([verify(num) for num in range(low, high + 1)])
