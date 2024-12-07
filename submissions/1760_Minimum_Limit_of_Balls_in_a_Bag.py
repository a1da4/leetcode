class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def valid(mid: int) -> bool:
            currOperations = 0
            for num in nums:
                currOperations += math.ceil(num / mid) - 1
                if currOperations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1

        return left

