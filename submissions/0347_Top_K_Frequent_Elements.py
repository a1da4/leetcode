from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = Counter()
        for num in nums:
            num2freq[num] += 1
        
        answer = []
        for num_freq in num2freq.most_common(k):
            num, freq = num_freq
            answer.append(num)

        return answer
