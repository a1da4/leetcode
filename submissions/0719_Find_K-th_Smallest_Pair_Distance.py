class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        def search(maxDist):
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > maxDist:
                    left += 1
                count += right - left
            return count

        while left < right:
            mid = (left + right) // 2
            if search(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left

