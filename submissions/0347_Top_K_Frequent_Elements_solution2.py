class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num2freq[0] for num2freq in Counter(nums).most_common(k)]
