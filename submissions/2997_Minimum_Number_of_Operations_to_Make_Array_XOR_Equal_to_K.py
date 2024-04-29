class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0

        for num in nums:
            curr = curr ^ num

        count = 0        
        while curr or k:
            if (curr % 2) != (k % 2):
                count += 1
            curr //= 2
            k //= 2

        return count

