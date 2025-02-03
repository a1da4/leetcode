class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:        

        def strictlyIncreasing(nums: List[int]) -> int:
            prev = nums[0]
            streak = 1
            maxStreak = 0
            for num in nums[1:]:
                if prev < num:
                    streak += 1
                else:
                    maxStreak = max(streak, maxStreak)
                    streak = 1
                prev = num
            return max(streak, maxStreak)

        return max(strictlyIncreasing(nums), strictlyIncreasing(nums[::-1]))

