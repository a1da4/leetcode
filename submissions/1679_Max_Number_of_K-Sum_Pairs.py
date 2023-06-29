class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftId = 0
        rightId = len(nums) - 1
        count = 0
        while leftId < rightId:
            currentSum = nums[leftId] + nums[rightId]
            if currentSum == k:
                leftId += 1
                rightId -= 1
                count += 1
            elif currentSum < k:
                leftId += 1
            else:
                rightId -= 1
        
        return count
