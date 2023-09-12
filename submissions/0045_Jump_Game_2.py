class Solution:
    def jump(self, nums: List[int]) -> int:
        currReach = 0
        currJumps = 0
        last = 0

        for i in range(len(nums)-1):
            currReach = max(currReach, i+nums[i])

            if i == last:
                last = currReach
                currJumps += 1
                        
        return currJumps
