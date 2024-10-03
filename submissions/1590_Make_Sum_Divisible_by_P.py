class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        totalMod = 0
        for num in nums:
            totalMod = (totalMod + num) % p
        target = totalMod % p
        if target == 0:
            return 0
        mod2id = {0: -1}
        currMod = 0
        minLen = N
        for i in range(N):
            currMod = (currMod + nums[i]) % p
            required = (currMod - target + p) % p
            if required in mod2id:
                minLen = min(minLen, i - mod2id[required])
            
            mod2id[currMod] = i

        return -1 if minLen == N else minLen

