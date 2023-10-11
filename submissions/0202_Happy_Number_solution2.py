class Solution:
    def isHappy(self, n: int) -> bool:

        def calculateNums(num: int) -> int:
            result = 0
            while num > 0:
                digit = num%10
                result += digit ** 2
                num = num // 10
            return result

        val = calculateNums(n)
        vals = set()
        while val > 1:
            val = calculateNums(val)
            if val in vals:
                return False
            vals.add(val)
        
        return val == 1
