class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for currId in range(len(nums)-1):
            if nums[currId+1] <= nums[currId]:
                diff = nums[currId] + 1 - nums[currId + 1]
                answer += diff
                nums[currId + 1] += diff
        return answer

