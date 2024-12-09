class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return N
        prev = nums[1] - nums[0]
        answer = 2 if prev != 0 else 1
        for i in range(2, N):
            curr = nums[i] - nums[i - 1]
            if (curr > 0 and prev <= 0) or (curr < 0 and prev >= 0):
                answer += 1
                prev = curr
        return answer

