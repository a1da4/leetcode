class Solution:
    def minCapability(self, nums, k):
        minReward, maxReward = min(nums), max(nums)
        N = len(nums)
        while minReward < maxReward:
            midReward = (minReward + maxReward) // 2

            currId = 0
            currHouses = 0
            while currId < N:
                if nums[currId] <= midReward:
                    currHouses += 1 
                    currId += 2
                else:
                    currId += 1
            
            if currHouses >= k:
                maxReward = midReward
            else:
                minReward = midReward + 1
 
        return minReward

