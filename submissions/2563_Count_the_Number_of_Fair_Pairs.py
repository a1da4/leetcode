class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def getLower(nums: List[int], 
                     left: int, 
                     right: int, 
                     target: int) -> int:
            while left <= right:
                mid = left + ((right - left) // 2)
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        nums.sort()
        N = len(nums)
        answer = 0
        for currId in range(N):
            left = getLower(nums, currId + 1, N - 1, lower - nums[currId])
            right = getLower(nums, currId + 1, N - 1, upper - nums[currId] + 1)
            answer += right - left

        return answer

