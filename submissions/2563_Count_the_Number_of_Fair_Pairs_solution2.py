class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()
        answer = 0
        for i in range(N):
            l = bisect.bisect_left(nums, lower  - nums[i], i+1, N)
            r = bisect.bisect_right(nums, upper  - nums[i], i+1, N)
            answer += r - l
        return answer

