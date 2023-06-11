class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numMatches = 0
        currentSum = 0
        dic = {0:1}
        for num in nums:
            currentSum = currentSum + num
            if currentSum-k in dic:
                numMatches = numMatches + dic[currentSum-k]
            if currentSum not in dic:
                dic[currentSum] = 1
            else:
                dic[currentSum] = dic[currentSum]+1

        return numMatches
