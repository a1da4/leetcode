class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num2freq = Counter(nums)
        answer = num2freq.most_common()[-1][0]
        return answer
