class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num2freq = Counter(nums)
        answer = 0
        maxFreq = None
        for (num, freq) in num2freq.most_common():
            if maxFreq is None:
                maxFreq = freq
                answer += freq
            elif freq == maxFreq:
                answer += freq
            else:
                break
        return answer
