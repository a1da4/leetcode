class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        dist2freq = {}
        answer = 0
        for i in range(N):
            dist = nums[i] - i
            if dist not in dist2freq:
                dist2freq[dist] = 0
            dist2freq[dist] += 1
        
        total = N
        for freq in dist2freq.values():
            answer += freq * (total - freq)
            total -= freq
        return answer
