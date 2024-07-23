class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []
        num2freq = Counter(nums)
        freq2nums = defaultdict(list)
        for num, freq in num2freq.items():
            freq2nums[freq].append(num)
        freqs = list(set(num2freq.values()))
        freqs.sort()
        for freq in freqs:
            nums = freq2nums[freq]
            for num in sorted(nums, reverse=True):
                answer = answer + [num] * freq
        
        return answer
