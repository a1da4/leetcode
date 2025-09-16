class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def LCM(num1: int, num2: int) -> int:
            return num1 * num2 // math.gcd(num1, num2)

        def isNonCoprime(num1: int, num2: int) -> bool:
            return math.gcd(num1, num2) > 1

        stack = []
        for num in nums:
            while stack and isNonCoprime(stack[-1], num):
                num = LCM(stack.pop(), num)
            else:
                stack.append(num)

        return stack

