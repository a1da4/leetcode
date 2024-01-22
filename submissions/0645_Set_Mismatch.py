class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupNum = Counter(nums).most_common(1)[0][0]
        vocab = set(nums)

        for num in range(1, len(nums)+1):
            if num not in vocab:
                return [dupNum, num]
