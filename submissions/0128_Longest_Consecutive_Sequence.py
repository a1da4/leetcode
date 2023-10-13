class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        vocab = set(nums)
        maxCon = 1
        currCon = 1
        for num in sorted(list(vocab)):
            if num - 1 in vocab:
                currCon += 1
            else:
                maxCon = max(currCon, maxCon)
                currCon = 1

        maxCon = max(currCon, maxCon)
        return maxCon
    
