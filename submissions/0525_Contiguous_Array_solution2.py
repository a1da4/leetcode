class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        x = 0
        maxLen = 0
        x2idx = {0: -1}

        for idx, num in enumerate(nums):
            x = x + 1 if num else x - 1

            if x in x2idx:
                maxLen = max(maxLen, idx - x2idx[x])            
            else:
                x2idx[x] = idx

        return maxLen
