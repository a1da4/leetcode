class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        N = len(nums)

        answer = 0
        for l in range(N):
            r = bisect.bisect_right(nums, target - nums[l]) - 1
            if r >= l:
                answer += pow(2, r - l, mod)

        return answer % mod

