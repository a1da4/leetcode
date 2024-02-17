class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numMatches = 0
        currentSum = 0
        dic = {0:1}
        vocab = set([0])
        for num in nums:
            currentSum = currentSum + num
            if currentSum-k in vocab:
                numMatches = numMatches + dic[currentSum-k]
            if currentSum not in vocab:
                dic[currentSum] = 1
                vocab.add(currentSum)
            else:
                dic[currentSum] = dic[currentSum]+1

        return numMatches
