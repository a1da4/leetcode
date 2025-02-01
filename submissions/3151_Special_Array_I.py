class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0] % 2
        for num in nums[1:]:
            curr = num % 2
            if prev == curr:
                return False
            prev = curr
        return True

