class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = 0
        mod2id = {0: -1}
        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            
            if mod in mod2id:
                if i - mod2id[mod] > 1:
                    return True
            else:
                mod2id[mod] = i
        
        return False
