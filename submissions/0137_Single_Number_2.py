class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num2freq = {}
        cands = []

        for num in nums:
            if num in num2freq:
                num2freq[num] = -1
                if num in cands:
                    cands.remove(num)
            else:
                num2freq[num] = 1
                cands.append(num)
        return cands[0]
