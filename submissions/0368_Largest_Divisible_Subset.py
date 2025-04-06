class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        dp = [0] * N
        prev = [None] * N
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        maxId = None
        maxNum = 0
        for i in range(N):
            if maxNum < dp[i]:
                maxId = i
                maxNum = dp[i]

        answer = []
        currId = maxId
        while currId is not None:
            answer.append(nums[currId])
            currId = prev[currId]

        return answer if answer else nums[0:1]

