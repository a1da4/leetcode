class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num2freq = Counter(nums)
        answer = 0
        for freq in num2freq.values():
            if freq == 1:
                return -1
            temp = freq // 3
            freq -= temp * 3
            answer += temp + freq // 2 + freq % 2
        return answer
