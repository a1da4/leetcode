class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        dist2freq = defaultdict(int)
        answer = 1

        for i in range(N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dist2freq[(i, diff)] = dist2freq.get((j, diff), 1) + 1
                answer = max(answer, dist2freq[(i, diff)])

        return answer

