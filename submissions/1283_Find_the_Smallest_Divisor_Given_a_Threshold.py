class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculate(divisor: int) -> int:
            sumOfDiv = 0
            for num in nums:
                sumOfDiv += num // divisor
                if num % divisor:
                    sumOfDiv += 1

            return sumOfDiv
        
        answer = -1
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            sod = calculate(m)
            if sod <= threshold:
                answer = m
                r = m - 1
            else:
                l = m + 1
        
        return answer

