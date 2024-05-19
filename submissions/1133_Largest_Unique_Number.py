class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num2freq = Counter(nums)
        answer = -1
        for num, freq in num2freq.most_common()[::-1]:
            if freq > 1:
                break
            answer = max(answer, num)
        return answer

