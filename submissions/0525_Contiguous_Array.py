class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        x = 0
        maxLen = 0
        idx = 0
        bit2idx = {0: -1}
        keys = [0]

        for num in nums:
            if num:
                x += 1
            else:
                x -= 1
            
            if bit2idx.get(x, bit2idx[keys[-1]]) != bit2idx[keys[-1]]:
                maxLen = max(maxLen, idx - bit2idx[x])
            else:
                if x not in bit2idx:
                    bit2idx[x] = idx
                    keys.append(x)
            
            idx += 1
        
        return maxLen
