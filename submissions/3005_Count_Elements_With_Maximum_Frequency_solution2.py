class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num2freq = Counter(nums)
        freq2freq = Counter(num2freq.values())
        maxFreq = max(num2freq.values())

        return maxFreq * freq2freq[maxFreq]
