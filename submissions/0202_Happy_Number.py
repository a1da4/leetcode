class Solution:
    def isHappy(self, n: int) -> bool:

        def separateNum(num: int) -> List[int]:
            nums = []
            while num > 0:
                nums.append(num%10)
                num = num // 10
            return nums
        
        def calculateNums(nums: List[int]) -> int:
            return sum([num**2 for num in nums])

        nums = separateNum(n)
        val = calculateNums(nums)
        vals = set()

        while val > 1:
            nums = separateNum(val)
            val = calculateNums(nums)
            if val in vals:
                return False
            vals.add(val)
        
        return val == 1
