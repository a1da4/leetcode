class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        N = len(nums)

        for i in range(N - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, N - 1):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                answer += k - j - 1

        return answer

