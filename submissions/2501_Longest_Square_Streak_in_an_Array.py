class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num2freq = defaultdict(int)
        answer = 0
        for num in nums:
            num2freq[num ** 2] = num2freq[num] + 1
            answer = max(answer, num2freq[num ** 2])

        if answer == 1:
            return -1
        else:
            return answer
